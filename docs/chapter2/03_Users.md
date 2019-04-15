用户部分
======

> 首次撰写：2017-11-14

> 最后修改：-

接口列表
------------

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/me/profile/](#profile) | GET / PUT|登录用户|设置用户信息|
| [/api/me/profile/avatar/](#address) | GET / PUT|登录用户|设置用户头像|
| [/api/me/profile/nick/](#profile) | GET / PUT|登录用户|设置用户昵称(马甲)|
| [/api/me/profile/emercontact/](#profile) | GET / PUT|登录用户|应急联系人|
| [/api/me/profile/balance/](#profile) | GET / PUT|登录用户|数字版额度|

<!-- | [/api/me/contains/](#contains) | GET / POST|登录用户|用户手机通讯录提交对比接口|
| [/api/me/contact/contains/](#contains) | POST | 登录用户 |上传通讯录|
| [/api/me/contact/{pk}/](#contact_detail) | GET / PUT / DELETE|登录用户 | 设置黑名单 |
| [/api/me/contact/black/](#contact_black) | POST | 登录用户 |批量隐藏我名字(批量)|
| [/api/me/contact/hide/](#contact_hide) | POST | 登录用户 | 批量隐藏我名字 |
| [/api/me/contact/black/](#contact_black_batch) | POST | 登录用户 | 批量黑名单 |
| [/api/me/notices/](#notices) | GET | 登录用户 | 消息中心 |
| [/api/me/bankcard/](#bankcard) | GET / PUT / DELETE|登录用户|银行卡| -->

<!-- | [/api/me/blacklist/](#blacklist) | GET / PUT / DELETE|登录用户|黑名单| -->

用户信息接口 (Profile)
------------

简要描述：
 - 用户信息接口

请求URL：
 - `http://<domain>/api/me/profile/`

请求方式：
 - `PUT` `GET`

请求权限：
 - `登录用户`

请求参数：
 - 仅 PUT 请求时使用参数 

| 参数名 | 必选	| 类型	| 备注 |
| :-- | :-- 	| :-- 	| |
| name | x	    | 字符	| 真名 |
| nick | x	    | 字符	| 昵称 |
| gender | x	    | 枚举	| 性别 male(男), female(女)	|
| birthday | x	    | 日期	| 生日 |
| friend_verify	| x | 布尔	| 加好友时是否验证 |
| mobile_verify | x | 布尔	| 是否允许手机号查找 |
| name_public 	| x | 布尔	| 是否公开姓名 |


返回示例:

```json
{
    "id": 4,
    "name": "",
    "nick": "",
    "phone": "",
    "gender": "male",
    "idcard": "",
    "birthday": null,
    "friend_verify": false,
    "mobile_verify": false,
    "name_public": false,
    "avatar": "http://moo.life:8809/media/avatar/default.jpg",
    "balance": "100.00"
}
```

返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|		|
| name			| 字符	| 真名	|
| nick			| 字符	| 昵称	|
| phone			| 电话	| 电话						|
| gender		| 枚举	| 性别 male(男), female(女)	|
| idcard		| 字符	| 银行卡		|
| birthday		| 日期	| 生日		|
| friend_verify	| 布尔	| 朋友验证	|
| mobile_verify | 布尔	| 手机是否验证	|
| name_public 	| 布尔	| 真名是否公开	|
| balance       | 货币   | 数字币余额  |
| avatar 		| 图片	| 头像图片	|

备注
 
 - 更多返回错误代码请看首页的错误代码描述


设置用户头像 (Avatar)
------------

简要描述：
 - 设置用户头像

请求URL：
 - `http://<domain>/api/me/profile/avatar/`

请求方式：
 - `PUT` `GET`

请求权限：
 - `登录用户`

请求参数：
 - 仅 PUT 请求时使用参数 

| 参数名			| 必选	| 类型	| 备注						|
| :-- 			| :--: 	| :-- 	|							|
| avatar 		| √	    | 图片	| 头像图片					|


返回示例:

```json
{
    "avatar": "http://<domian>/media/avatar/default.jpg"
}
```

返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|		|
| avatar 		| 图片	| 头像图片	|

备注
 
 - 更多返回错误代码请看首页的错误代码描述



设置用户昵称 (Nick)
------------

简要描述：
 - 设置用户头像

请求URL：
 - `http://<domain>/api/me/profile/nick/`

请求方式：
 - `PUT` `GET`

请求权限：
 - `登录用户`

请求参数：
 - 仅 PUT 请求时使用参数 

| 参数名			| 必选	| 类型	| 备注						|
| :-- 			| :--: 	| :-- 	|							|
| nick 			| √	    | 字符	| 昵称					|


返回示例:

```json
{
    "nick": "张三"
}
```

返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|		|
| nick 			| 字符	| 昵称	|

备注
 
 - 更多返回错误代码请看首页的错误代码描述

