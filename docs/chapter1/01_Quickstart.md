快速开始
=======

开发指南
-------

特别说明：

- 注册，登录的测试接口表单，默认显示json数据结构。
- 增加一个测试的高级管理账号 `admin` 密码 `admin`。
- 更新测试 [http://10.7.7.22:3000/api/](http://10.7.7.22:3000/api/)

> 问题：接口方面 补全下数据吧 比如说 烦null的地方 比如说反数组的地方 加数据吧 否则不知道怎么解析
> 解答：如果是空列表数据则会返回以下结构，直接解析json就可以了，判断results 是否空即可。

```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": [

    ]
}
```

> 如果是单条空数据 则会返回以下内容，直接解析json就可以了，判断是否有detail，有则为空数据，或者有异常错误的数据。

```json
{
    "detail": "你要找的内容不存在。"
}
```

调试工具
-------

- curl [使用方法](http://ju.outofmemory.cn/entry/84875)
- http [安装方法](http://yhz.me/blog/use-httpie.html)
- 另外还有个图形化测试工具 [RestClient](http://www.oschina.net/p/restclient)
- 或者使用`firefox` 的 `RestClient` 插件。
- 谷歌浏览器可以使用 `postman`
- MacOS 系统下 `paw`
- Android Studio 下 `RestClient` 工具
- 调试工具很多, 可以根据自身喜好选用。

抓包工具
-------
- Charles (支持 Windows 和 MacOS, 收费 有破解版)
- Fiddler (仅支持 Windows, 更 Charles 类似)
- Wireshark (支持 Windows 和 MacOS, 免费, 使用门槛比较高)

调试方法
-------

这里主要以http为主，各位高手可以举一反三，呵呵。

```
http [method] [url]
```

> 注意：关于api的GET参数说明，api后面跟随的`{pk}`或者`{id}` 是一个意思，代表改资源(`resource`)的主键.


