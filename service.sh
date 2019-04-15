#!/bin/bash

pushd `dirname $0` > /dev/null
BASEDIR=`pwd`
popd > /dev/null

init() {
    mkdir -p runtime/log/ims
    mkdir -p runtime/log/imr
    mkdir -p runtime/log/im
    mkdir -p runtime/tmp/im
    mkdir -p runtime/tmp/pending
}

start() {
    nohup $BASEDIR/bin/ims -log_dir=runtime/log/ims ims.cfg >runtime/log/ims/ims.log 2>&1 &
    nohup $BASEDIR/bin/imr -log_dir=runtime/log/imr imr.cfg >runtime/log/imr/imr.log 2>&1 &
    nohup $BASEDIR/bin/im -log_dir=runtime/log/im im.cfg >runtime/log/im/im.log 2>&1 &
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
