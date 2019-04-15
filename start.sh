#!/bin/bash

pushd `dirname $0` > /dev/null
BASEDIR=`pwd`
popd > /dev/null

init() {
    mkdir -p /var/log/ims
    mkdir -p /var/log/imr
    mkdir -p /var/log/im
    mkdir -p /var/tmp/im
    mkdir -p /var/tmp/pending
}

start() {
    nohup $BASEDIR/bin/ims -log_dir=/var/log/ims ims.cfg > /var/log/ims/ims.log 2 >&1 &
    nohup $BASEDIR/bin/imr -log_dir=/var/log/imr imr.cfg > /var/log/imr/imr.log 2 >&1 &
    nohup $BASEDIR/bin/im  -log_dir=/var/log/im  im.cfg  > /var/log/im/im.log   2 >&1 &
}

stop() {
    killall im
    killall ims
    killall imr
}

case "$1" in
    start)
        start
        ;;

    stop)
        stop
        ;;
    init)
        init
        ;;
    *)
        echo $"Usage: $0 {start|init|stop}"
        exit 2
esac
