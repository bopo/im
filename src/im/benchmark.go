package main

import "fmt"
import "net"
import "log"
import "runtime"
import "time"
import "flag"
import "strings"
import "io/ioutil"
import "net/http"
import "encoding/base64"
import "crypto/md5"
import "encoding/json"
import "github.com/bitly/go-simplejson"

const HOST = "127.0.0.1"
const PORT = 23000

const APP_ID = 7
const APP_KEY = "sVDIlIiDUm7tWPYWhi6kfNbrqui3ez44"
const APP_SECRET = "0WiCxAU1jh76SbgaaFC7qIaBPm2zkyM1"
const URL = "http://192.168.33.10:5000"

var concurrent int
var count int
var c chan bool

func init() {
	flag.IntVar(&concurrent, "c", 10, "concurrent number")
	flag.IntVar(&count, "n", 100000, "request number")
}

func login(uid int64) string {
	url := URL + "/auth/grant"
	secret := fmt.Sprintf("%x", md5.Sum([]byte(APP_SECRET)))
	s := fmt.Sprintf("%d:%s", APP_ID, secret)
	basic := base64.StdEncoding.EncodeToString([]byte(s))

	v := make(map[string]interface{})
	v["uid"] = uid

	body, _ := json.Marshal(v)

	client := &http.Client{}
	req, _ := http.NewRequest("POST", url, strings.NewReader(string(body)))
	req.Header.Set("Authorization", "Basic "+basic)
	req.Header.Set("Content-Type", "application/json; charset=UTF-8")

	res, err := client.Do(req)
	if err != nil {
		return ""
	}
	defer res.Body.Close()

	b, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return ""
	}
	obj, err := simplejson.NewJson(b)
	token, _ := obj.Get("data").Get("token").String()
	return token
}

func send(uid int64, receiver int64, sem chan int) {
	ip := net.ParseIP(HOST)
	addr := net.TCPAddr{ip, PORT, ""}

	token := login(uid)

	if token == "" {
		panic("")
	}

	conn, err := net.DialTCP("tcp4", nil, &addr)
	if err != nil {
		log.Println("connect error")
		return
	}
	seq := 1
	auth := &AuthenticationToken{token: token, platform_id: 1, device_id: "00000000"}
	_ = SendMessage(conn, &Message{cmd: MSG_AUTH_TOKEN, seq: seq, version: DEFAULT_VERSION, body: auth})
	ReceiveMessage(conn)

	sendCount := 0
	for i := 0; i < count; i++ {
		content := fmt.Sprintf("test....%d", i)
		seq++
		msg := &Message{MSG_IM, seq, DEFAULT_VERSION, 0,
			&IMMessage{uid, receiver, 0, int32(i), content}}

		select {
		case <-sem:
			break
		case <-time.After(1 * time.Second):
			log.Println("wait send sem timeout")
		}

		_ = SendMessage(conn, msg)

		var ack *Message
		for {
			mm := ReceiveMessage(conn)
			if mm == nil {

				break
			}
			if mm.cmd == MSG_ACK {
				ack = mm
				break
			}
		}

		if ack != nil {
			sendCount++
		} else {
			log.Println("recv ack error")
			break
		}
	}
	_ = conn.Close()
	c <- true
	log.Printf("%d send complete:%d", uid, sendCount)
}

func receive(uid int64, limit int, sem chan int) {
	syncKey := int64(0)

	ip := net.ParseIP(HOST)
	addr := net.TCPAddr{ip, PORT, ""}

	token := login(uid)

	if token == "" {
		panic("")
	}

	conn, err := net.DialTCP("tcp4", nil, &addr)
	if err != nil {
		log.Println("connect error")
		return
	}
	seq := 1
	auth := &AuthenticationToken{token: token, platform_id: 1, device_id: "00000000"}
	_ = SendMessage(conn, &Message{MSG_AUTH_TOKEN, seq, DEFAULT_VERSION, 0, auth})
	ReceiveMessage(conn)

	seq++
	ss := &Message{MSG_SYNC, seq, DEFAULT_VERSION, 0, &SyncKey{syncKey}}
	_ = SendMessage(conn, ss)

	//一次同步的取到的消息数目
	syncCount := 0

	recvCount := 0
	syncing := false
	pendingSync := false

	for {
		if limit > 0 {
			_ = conn.SetDeadline(time.Now().Add(40 * time.Second))
		} else {
			_ = conn.SetDeadline(time.Now().Add(400 * time.Second))
		}

		msg := ReceiveMessage(conn)
		if msg == nil {
			log.Println("receive nill message")
			break
		}

		if msg.cmd == MSG_SYNC_NOTIFY {
			if !syncing {
				seq++
				s := &Message{MSG_SYNC, seq, DEFAULT_VERSION, 0, &SyncKey{syncKey}}
				_ = SendMessage(conn, s)
				syncing = true
			} else {
				pendingSync = true
			}
		} else if msg.cmd == MSG_IM {
			//m := msg.body.(*IMMessage)
			//log.Printf("sender:%d receiver:%d content:%s", m.sender, m.receiver, m.content)

			recvCount += 1
			if limit > 0 && recvCount <= limit {
				select {
				case sem <- 1:
					break
				case <-time.After(10 * time.Millisecond):
					log.Println("increment timeout")
				}
			}

			syncCount++

			seq++
			ack := &Message{MSG_ACK, seq, DEFAULT_VERSION, 0, &MessageACK{int32(msg.seq)}}
			SendMessage(conn, ack)
		} else if msg.cmd == MSG_SYNC_BEGIN {
			syncCount = 0
			//log.Println("sync begin:", recv_count)
		} else if msg.cmd == MSG_SYNC_END {
			syncing = false
			s := msg.body.(*SyncKey)
			//log.Println("sync end:", recv_count, s.sync_key, sync_key)			
			if s.sync_key > syncKey {
				syncKey = s.sync_key
				//log.Println("sync key:", sync_key)
				seq++
				sk := &Message{MSG_SYNC_KEY, seq, DEFAULT_VERSION, 0, &SyncKey{syncKey}}
				SendMessage(conn, sk)
			}

			if limit < 0 && syncCount == 0 {
				break
			}

			if limit > 0 && recvCount >= limit {
				break
			}

			if pendingSync {
				seq++
				s := &Message{MSG_SYNC, seq, DEFAULT_VERSION, 0, &SyncKey{syncKey}}
				SendMessage(conn, s)
				syncing = true
				pendingSync = false
			}

		} else {
			log.Println("mmmmmm:", Command(msg.cmd))
		}
	}
	conn.Close()
	c <- true

	log.Printf("%d received:%d", uid, recvCount)
}

func main() {
	runtime.GOMAXPROCS(4)
	flag.Parse()

	fmt.Printf("concurrent:%d, request:%d\n", concurrent, count)

	log.SetFlags(log.Lshortfile | log.LstdFlags)

	c = make(chan bool, 100)
	u := int64(13635273140)

	sems := make([]chan int, concurrent)

	for i := 0; i < concurrent; i++ {
		sems[i] = make(chan int, 2000)
		for j := 0; j < 1000; j++ {
			sems[i] <- 1
		}
	}

	//接受历史离线消息
	for i := 0; i < concurrent; i++ {
		go receive(u+int64(concurrent+i), -1, sems[i])
	}

	for i := 0; i < concurrent; i++ {
		<-c
	}

	time.Sleep(1 * time.Second)

	//启动接受者
	for i := 0; i < concurrent; i++ {
		go receive(u+int64(concurrent+i), count, sems[i])
	}

	time.Sleep(2 * time.Second)

	begin := time.Now().UnixNano()
	log.Println("begin test:", begin)

	for i := 0; i < concurrent; i++ {
		go send(u+int64(i), u+int64(i+concurrent), sems[i])
	}
	for i := 0; i < 2*concurrent; i++ {
		<-c
	}

	end := time.Now().UnixNano()

	var tps int64 = 0
	if end-begin > 0 {
		tps = int64(1000*1000*1000*concurrent*count) / (end - begin)
	}
	fmt.Println("tps:", tps)
}
