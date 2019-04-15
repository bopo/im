其他
======

> 首次撰写：2018-1-8

> 最后修改：-

接口列表
------------

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/feedback/](#feedback) | GET |登录用户|意见反馈接口|
| [/api/banner/](#banner) | GET |登录用户|广告管理接口|
| [/api/faq/](#faq) | GET |登录用户|用户帮助接口|
| [/api/about/](#about) | GET |登录用户|关于我们接口|

意见反馈接口 (feedback)
-----


简要描述：
 -

请求URL：
 - `http://<domain>/api/feedback/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|id  |int   |自增ID |
|title  |varchar   | 标题 |
|phone   |varchar   |联系电话 |
|content   |text   |	内容详情 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "created": "2017-12-04 02:22:57",
            "modified": "2017-12-04 02:22:57",
            "title": "2345",
            "phone": "2345",
            "content": "2345"
        }
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述

广告管理接口 (banner)
-----


简要描述：
 -

请求URL：
 - `http://<domain>/api/banner/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|id  |int   |自增ID |
|title  |varchar   | 标题 |
|picurl   |image   |图片 |
|content   |text   |	内容详情 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "created": "2017-11-19 20:37:31",
            "modified": "2017-11-19 20:37:31",
            "title": "1",
            "content": "1111",
            "picurl": "http://127.0.0.1:8080/media/goods/QQ%E6%88%AA%E5%9B%BE20171031154818.jpg",
            "order": 1
        }
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述

 用户帮助接口 (faq)
-----


简要描述：
 -

请求URL：
 - `http://<domain>/api/faq/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|id  |int   |自增ID |
|title  |varchar   | 标题 |
|picurl   |image   |图片 |
|content   |text   |	内容详情 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
           "id": 1,
            "created": "2017-11-19 20:38:04",
            "modified": "2017-11-19 20:38:04",
            "title": "123",
            "content": "1111",
            "picurl": "http://127.0.0.1:8080/media/goods/QQ%E6%88%AA%E5%9B%BE20171031154818_cOnnLWE.jpg"
        }
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述

 关于我们接口 (about)
-----


简要描述：
 -

请求URL：
 - `http://<domain>/api/about/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|id  |int   |自增ID |
|title  |varchar   | 标题 |
|picurl   |image   |图片 |
|content   |text   |	内容详情 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
          "id": 1,
            "created": "2017-11-19 20:38:04",
            "modified": "2017-11-19 20:38:04",
            "title": "123",
            "content": "1111",
            "picurl": "http://127.0.0.1:8080/media/goods/QQ%E6%88%AA%E5%9B%BE20171031154818_cOnnLWE.jpg"
        }
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述