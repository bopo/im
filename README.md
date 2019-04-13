
# im service
1. 支持点对点消息, 群组消息, 聊天室消息
2. 支持集群部署
3. 单机支持50w用户在线
4. 单机处理消息5000条/s
5. 支持超大群组(3000人)

*服务器硬件指标：32g 16核*

## 编译运行

1. 安装go编译环境

   参考链接:https://golang.org/doc/install

2. 下载im_service代码

   cd $GOPATH/src/github.com/GoBelieveIO

   git clone https://github.com/GoBelieveIO/im_service.git

3. 安装依赖

   cd im_service

   dep ensure

4. 编译

   cd im_service
    
   mkdir bin
    
   make install
    
   可执行程序在bin目录下

5. 安装mysql数据库, redis, 并导入db.sql

6. 配置程序
   配置项的说明参考ims.cfg.sample, imr.cfg.sample, im.cfg.sample

7. 启动程序

  * 创建配置文件中配置的im&ims消息存放路径

    mkdir -p ./runtime/tmp/im
    mkdir -p ./runtime/tmp/impending

  * 创建日志文件路径
    
    mkdir -p ./runtime/data/logs/ims
    mkdir -p ./runtime/data/logs/imr
    mkdir -p ./runtime/data/logs/im

  * 启动im服务

    pushd \`dirname $0\` > /dev/null

    BASEDIR=\`pwd\`

    nohup $BASEDIR/ims -log_dir=./logs/ims ims.cfg >./logs/ims/ims.log 2>&1 &
    nohup $BASEDIR/imr -log_dir=./logs/imr imr.cfg >./logs/imr/imr.log 2>&1 &
    nohup $BASEDIR/im -log_dir=./logs/im im.cfg >./logs/im/im.log 2>&1 &

    ./bin/ims -log_dir=./log/ims cfg/ims.cfg >./log/ims/ims.log 2>&1 &
    ./bin/imr -log_dir=./log/imr cfg/imr.cfg >./log/imr/imr.log 2>&1 &
    ./bin/im -log_dir=./log/im cfg/im.cfg >./log/im/im.log 2>&1 &

## token的格式

    连接im服务器token存储在redis的hash对象中,脱离API服务器测试时，可以手工生成。
    $token就是客户端需要获得的, 用来连接im服务器的认证信息。
    key:access_token_$token
    field:
        user_id:用户id
        app_id:应用id


## 官方QQ群
1. 450359487，加群请附加说明信息。

## 官方网站
   https://developer.gobelieve.io/

## 相关产品
   https://goubuli.mobi/
