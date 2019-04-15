部署说明
==========

系统依赖
-------
1. linux 发行版 (centos，debian等)，推荐 debian 8.6.x 以及以上

部署前的软件安装
-------------

### 安装 pyenv

```
sudo apt-get install libreadline-dev libbz2-dev libsqlite3-dev libssl-dev
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

### 安装 python

```
v=3.6.3|wget -c http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/;pyenv install $v
```

### 安装 nginx
```
sudo apt-get install nginx
```

### 安装 postgresql 或者 mysql

```
sudo apt-get install postgresql
// or
sudo apt-get install mysql-server
```

### 安装 supervisor
```
sudo apt-get install supervisor

```

部署前的配置
----------
1. 配置 volumes(磁盘卷) ，已经配置好了，除特殊情况不需要修改
2. 配置暴露端口 ports 在 docker-compose.yml 选项，已经配置好了，除特殊情况不需要修改

全局的配置在代码根目录下的 env.server 复制为 .env 文件，需要配置的选项如下 ：

> _**需要注意的是, 配置 ”=“ 前后不能有空格 (具体选项可能有变动)**_

```bash
# 项目默认的用户名和密码
DJANGO_ADMIN_USER=bankeys
DJANGO_ADMIN_PASS=secret

# 融云相关配置
RONGCLOUD_APPKEY=ik1qhw09ifflp
RONGCLOUD_SECRET=kfx3v7mffJeaJt

# jpush 相关配置
JPUSH_APPKEY=496daf24808978b12e4e0505
JPUSH_SECRET=6e449bd8dd4dd2e5dff00c02

# 四要素认证相关配置, 如果更改可以联系开发二部
IDDENTITY_APPKEY=69tx91g3kpzlqkndszzofj38fr
IDDENTITY_GATEWAY=https://10.7.7.71:3002/api/register

# 验签微服务, 无特殊情况不需要修改
VERIFY_GATEWAY=http://verifysign:8080

# 验证银行 PIN 码微服务, 无特殊情况不需要修改
BANK_CARD=http://bankcard:5000/bank
```

## 部署环境步骤

```bash
/etc/init.d/supervisord restart
```

## 数据备份与维护
待续


