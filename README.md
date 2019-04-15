
# IM 即时通讯服务器

## 项目特点
1. 支持点对点消息, 群组消息, 聊天室消息
2. 支持集群部署
3. 单机支持50w用户在线
4. 单机处理消息5000条/s
5. 支持超大群组(3000人)

*服务器硬件指标：32g 16核*

## 编译运行

1. 安装go编译环境

   参考链接:https://golang.org/doc/install
   pip install honcho redis pymysql mongo pytest

2. 下载im_service代码

   cd $GOPATH/src/github.com/bopo

   git clone https://github.com/bopo/im.git

3. 安装依赖
```
cd im && dep ensure -v
```
4. 编译
```
cd im
mkdir bin
make install
```    
可执行程序在bin目录下

5. 安装mysql数据库, redis, 并导入db.sql

6. 配置程序
   配置项的说明参考ims.cfg.sample, imr.cfg.sample, im.cfg.sample

7. 启动程序

## 创建配置文件中配置的im&ims消息存放路径
```
mkdir -p ./runtime/tmp/im
mkdir -p ./runtime/tmp/impending

// or

make init
```

## 创建日志文件路径
```
mkdir -p ./runtime/log/ims
mkdir -p ./runtime/log/imr
mkdir -p ./runtime/log/im

// or

make init
```

## 编译不同系统
```
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 make    // linux
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 make   // macos
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 make  // windows
```  

## 启动im服务
```
# 自动后台执行
pushd \`dirname $0\` > /dev/null
BASEDIR=\`pwd\`

nohup $BASEDIR/ims -log_dir=./runtime/log/ims ims.cfg >./runtime/log/ims/ims.log 2>&1 &
nohup $BASEDIR/imr -log_dir=./runtime/log/imr imr.cfg >./runtime/log/imr/imr.log 2>&1 &
nohup $BASEDIR/im -log_dir=./runtime/log/im im.cfg >./runtime/log/im/im.log 2>&1 &

# 手动执行
./bin/ims -log_dir=./runtime/log/ims cfg/ims.cfg >./runtime/log/ims/ims.log 2>&1 &
./bin/imr -log_dir=./runtime/log/imr cfg/imr.cfg >./runtime/log/imr/imr.log 2>&1 &
./bin/im -log_dir=./runtime/log/im cfg/im.cfg >./log/runtime/im/im.log 2>&1 &
```
## token的格式

连接`IM`服务器`token`存储在`redis`的`hash`对象中,脱离`API`服务器测试时，可以手工生成。
`$token`就是客户端需要获得的, 用来连接im服务器的认证信息。

```
key:access_token_$token
field:
    user_id:用户id
    app_id:应用id
```
