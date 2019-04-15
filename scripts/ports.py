# -*- coding:utf-8 -*-
import click
import socket

def net_is_used(port, ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
        s.shutdown(2)
        click.secho(u'[√] %s:%d is open' % (ip,port), fg='green')
        return True
    except:
    	click.secho(u'[x] %s:%d is close' % (ip,port), fg='yellow')
        return False

def main():
	port = [13333, 4444, 13890, 14890, 13891, 14891, 6666, 6665, 3334, 23000]
	
    for p in port:
		net_is_used(p)

if __name__ == '__main__':
	main()