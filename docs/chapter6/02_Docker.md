# 部署说明

## 系统依赖
1. 任意可以安装 docker 的 linux 发行版 (centos，debian等)，推荐 debian 8.6.x
2. docker >= 1.12.0
3. docker-compose >= 1.9.0


## 部署前的配置
1. 配置 volumes(磁盘卷) ，已经配置好了，除特殊情况不需要修改
2. 配置暴露端口 ports 在 docker-compose.yml 选项，已经配置好了，除特殊情况不需要修改

全局的配置在代码根目录下的 env.docker 复制为 .env 文件

## 部署环境步骤
1. 确保系统依赖和配置以及完成；
2. 在项目的根目录下执行: `docker-compose up --build` (第一次执行可以不加 `--build`). 如果没有提示报错在表示成功启动。
3. 启动后的数据初始化操作，具体操作如下：

```bash
# 第一次执行可以不加 `--build`
docker-compose up --build 
```

## 数据备份与维护
待续


