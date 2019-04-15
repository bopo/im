App相关
======

> 首次撰写：2017-11-14

> 最后修改：-

接口列表
------------

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/version/](#version) | GET   | 任意用户  | 安卓版本更新接口 |      
| [/api/feedback/](#feedback) | POST | 登录用户 | 意见反馈 |
| [/api/banner/](#banner) | GET | 登录用户 | 广告管理 |
| [/api/faq/](#faq) | GET | 登录用户 | 用户帮助 |


移动端版本更新接口 (Version)
------------

简要描述：
 - APP版本更新接口

请求URL：
 - `http://<domain>/api/version/`

请求方式：
 - `GET`

请求权限：
 - `任意用户`

| 参数名 | 必选  | 类型    | 备注        |
| :--   | :--   | :--   |           |
| platform  | √ | 字符    | 所属平台 (android, ios) 全小写   |

返回示例:

```json
{
    "version": "",
    "platform": "android",
    "depends": "",
    "install": null,
    "sha1sum": "",
    "channel": null,
    "constraint": false,
    "summary": ""
}
```

返回参数:

| 参数名 | 类型 | 备注 |
| :--   | :-- |     |
| platform  | 字符 | 所属平台 Android 或 iOS |
| version  | 字符 | 当前版本  |
| depends  | 字符 | 依赖版本  |
| install  | 字符 | 安装路径 URL  |
| sha1sum  | 字符 | 文件哈希  |
| channel  | 字符 | 安装渠道(点子市场)  |
| constraint  | 布尔值 | 是否强行更新  |
| summary  | 字符 | 更新说明  |

备注
 
 - 更多返回错误代码请看首页的错误代码描述

意见反馈接口(feedback)
------------

简要描述：
 - 意见反馈接口

请求URL：
 - `http://<domain>/api/feedback/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`


请求参数：
 - 仅 POST 请求时使用参数

| 参数名			| 必选	| 类型	| 备注						|
| :-- 			| :--: 	| :-- 	|							|
| title	    | √	    | 字符	| 标题 	|
| content	| √	    | 文本	| 内容详情 	|
| phone	    | √	    | 数字	| 联系电话 	|

返回示例:

```json
{
    "id": 4,
    "created": "2017-11-20 01:56:45",
    "modified": "2017-11-20 01:56:45",
    "title": "1",
    "content": "1",
    "phone": "1"
}
```

返回参数:

| 参数名		| 类型	| 备注		|
| :--		| :--	|			|
| title	| 字符	| 标题 	|
| content	| 文本	| 内容详情 	|
| phone	| 数字	| 联系电话 	|
| created	| 日期	| 创建时间 	|
| modified	| 日期	| 修改时间  |


备注
 
 - 更多返回错误代码请看首页的错误代码描述


广告管理接口(banner)
------------

简要描述：
 - 广告管理接口

请求URL：
 - `http://<domain>/api/banner/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`



返回示例:

```json
{
    "id": 1,
    "created": "2017-11-19 20:37:31",
    "modified": "2017-11-19 20:37:31",
    "title": "1",
    "content": "1111",
    "picurl": "http://127.0.0.1:8080/media/goods/QQ%E6%88%AA%E5%9B%BE20171031154818.jpg",
    "order": 1
}
```

返回参数:

| 参数名		| 类型	| 备注		|
| :--		| :--	|			|
| title	| 字符	| 标题 	|
| content	| 文本	| 内容详情 	|
| picurl	| 图片	| banner图片 	|
| created	| 日期	| 创建时间 	|
| modified	| 日期	| 修改时间  |
| order	| 字符	| 排序  |


备注

 - 更多返回错误代码请看首页的错误代码描述


 用户帮助接口(faq)
------------

简要描述：
 - 用户帮助接口

请求URL：
 - `http://<domain>/api/faq/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`


返回示例:

```json
{
    "id": 1,
    "created": "2017-11-19 20:38:04",
    "modified": "2017-11-19 20:38:04",
    "title": "123",
    "content": "1111",
    "picurl": "http://127.0.0.1:8080/media/goods/QQ%E6%88%AA%E5%9B%BE20171031154818_cOnnLWE.jpg"
}
```

返回参数:

| 参数名		| 类型	| 备注		|
| :--		| :--	|			|
| title	| 字符	| 标题 	|
| content	| 文本	| 内容详情 	|
| picurl	| 图片	| 帮助文档图片 |
| created	| 日期	| 创建时间 	|
| modified	| 日期	| 修改时间  |


备注

 - 更多返回错误代码请看首页的错误代码描述