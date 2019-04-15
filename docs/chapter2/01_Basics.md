基础部分(部分文档更新中)
====================

> 首次撰写：2017-11-14

> 最后修改：-

APP版本更新接口
-------
| 接口| 方法	| 权限| 备注			|
| :-- | :-- | :--|	:--|
| [/api/version/](#version) | GET	| 任意用户	| 安卓版本更新接口			|
|[/api/cards/<card\>](#card)|GET|登录用户|银行卡类型 <card\>:银行卡号|


用户搜索接口 (Users)
------------

| 接口						| 方法	| 权限 		| 备注 			|
| :-- 						| :--	| :--  		|:--			|
| [/api/users/](#users)				| GET	| 登录用户 	| 用户搜索(列表) 	|
| [/api/users/[id]/](#detail) 		| GET	| 登录用户 	| 用户详情 		|
| [/api/users/[id]/report/](#report)	| GET 	| 登录用户 	| 为举报接口		|
| [/api/users/[id]/invite/](#invite)	| GET 	| 登录用户 	| 邀请加好友		|
| [/api/users/[id]/confirm/](#confirm)| GET 	| 登录用户 	| 邀请好友确认		|


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

| 参数名 | 必选	| 类型	| 备注		|
| :--   | :-- 	| :-- 	|			|
| platform  | √ | 字符	| 所属平台 (android, ios) 全小写	|

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

| 参数名 | 类型 | 备注	|
| :--   | :-- |		|
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



银行卡类型 (Card)
------------

简要描述：
 - 银行卡类型查询

请求URL：
 - `http://<domain>/api/cards/{card}`

请求方式：
 - `GET`

请求权限：
 - `登录用户`



返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
| bank			| 字符	| 银行	|
| type			| 字符	| 卡类型	|

备注

 - 更多返回错误代码请看首页的错误代码描述

