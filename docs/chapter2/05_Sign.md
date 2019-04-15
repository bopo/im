
身份认证接口
==========


> 首次撰写：2017-11-14

> 最后修改：-

### 接口列表

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|[/api/sign/history/](#history)|GET|登录用户|签名历史, 签名详情|
|[/api/sign/identity/](#identity)|POST|登录用户|多要素身份认证接，文档暂缺。可以点击这里看接口页面 [详情](http://10.7.7.22:3000/api/sign/identity/)|
|[/api/sign/contract/](#contract)|POST|登录用户|合约接口，文档暂缺。可以点击这里看接口页面 [详情](http://10.7.7.22:3000/api/sign/contract/)|
|[/api/sign/transfer/](#transfer)|POST|登录用户|转账接口，文档暂缺。可以点击这里看接口页面 [详情](http://10.7.7.22:3000/api/sign/transfer/)|


合约接口接口 (Contract)
------------

简要描述：
 - 合约接口接口

请求URL：
 - `http://<domain>/api/sign/contract/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数：
 - 仅 POST 请求时使用参数


| 参数名 | 必填 | 类型 | 备注|
| :-- | :-- | :-- |:-- |
| created   | √     | 字符 | 创建时间 |
| modified  | √     | 字符 | 修改时间 |
| type      | √     | 字符 | 合约类型 |
| mobile    | √     | 电话 | 电话号码 |
| summary   | √     | 字符 | 合约备注 |
| make_date | √     | 字符 | 发生时间 |
| qrcode    | √     | 字符 | 合约二维码 |

返回示例:
* 列表返回格式

```json
{
    "count": 15,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 15,
            "created": "2017-12-08 20:29:20",
            "modified": "2017-12-08 20:29:20",
            "type": "contract",
            "mobile": "12313",
            "amount": "123123.00",
            "summary": "123123",
            "make_date": null,
            "orderid": "123123",
            "payment": "123123",
            "receipt": "123123",
            "payment_bank": "123123",
            "receipt_bank": "123123123"
        }
        ...
}
```

* 提交后返回格式

```json
{
    "id": 16,
    "created": "2017-12-08 20:36:02",
    "modified": "2017-12-08 20:36:02",
    "type": "",
    "summary": "1212",
    "make_date": null,
    "orderid": "2323",
    "qrcode": "http://127.0.0.1:5000/qr/eyJ0eXBlIjogInRyYW5zZmVyIiwgInN0YXR1cyI6ICJub3JtYWwiLCAidXJpIjogIi9hcGkvc2lnbi9jb250cmFjdC8iLCAiaWQiOiAxNn0=/"
}
```

返回参数:

| 参数名     | 类型 | 备注   |
| :--       | :--: | :--   |
| created   | 字符 | 创建时间 |
| modified  | 字符 | 修改时间 |
| type      | 字符 | 合约类型 |
| mobile    | 电话 | 电话号码 |
| summary   | 字符 | 合约备注 |
| make_date | 字符 | 发生时间 |
| qrcode    | 字符 | 合约二维码 |


备注

 - 更多返回错误代码请看首页的错误代码描述


转账收款接口 (Transfer)
------------

简要描述：
 - 合约收款接口

请求URL：
 - `http://<domain>/api/sign/transfer/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数：
 - 仅 POST 请求时使用参数


| 参数名 | 必填 | 类型 | 备注 |
| :-- | :-- | :-- | :-- |
| type | √ | 字符 | 合约类型 transfer |
| mobile | X | 电话 | 电话号码 |
| summary | √ | 字符 | 合约备注 |
| make_date | √ | 字符 | 发生时间 |
| payment | √ | 字符 | 支付银行账户 |
| receipt | √ | 字符 | 收款银行账户 |
| orderid | X | 字符 | 订单号 |


返回示例:
* 列表返回格式

```json
{
    "count": 15,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 15,
            "created": "2017-12-08 20:29:20",
            "modified": "2017-12-08 20:29:20",
            "type": "contract",
            "mobile": "12313",
            "amount": "123123.00",
            "summary": "123123",
            "make_date": null,
            "orderid": "123123",
            "payment": "123123",
            "receipt": "123123",
            "payment_bank": "123123",
            "receipt_bank": "123123123"
        }
        ...
}
```

* 提交后返回格式

```json
{
    "id": 16,
    "created": "2017-12-08 20:36:02",
    "modified": "2017-12-08 20:36:02",
    "type": "transfer",
    "mobile": "1212",
    "amount": "1212.00",
    "summary": "1212",
    "make_date": null,
    "orderid": "2323",
    "payment": "",
    "receipt": "",
    "payment_bank": "",
    "receipt_bank": "",
    "qrcode": "http://127.0.0.1:5000/qr/eyJ0eXBlIjogInRyYW5zZmVyIiwgInN0YXR1cyI6ICJub3JtYWwiLCAidXJpIjogIi9hcGkvc2lnbi9jb250cmFjdC8iLCAiaWQiOiAxNn0=/"
}
```

返回参数:

| 参数名 | 类型 | 备注 |
| :-- | :-: | :-- |
| created | 字符 | 创建时间 |
| modified | 字符 | 修改时间 |
| type | 字符 | 合约类型 |
| mobile | 电话 | 电话号码 |
| amount | 货币 | 转账金额 |
| orderid | 字符 | 订单号 |
| payment | 字符 | 支付银行账户 |
| receipt | 字符 | 收款银行账号 |
| payment_bank | 字符 | 支付银行名称 |
| receipt_bank | 字符 | 收款银行名称 |
| summary | 字符 | 合约备注 |
| make_date | 字符 | 发生时间 |
| qrcode | 字符 | 合约二维码 |


备注

 - 更多返回错误代码请看首页的错误代码描述


签名历史接口 (History)
------------

简要描述：
 - 签名历史接口

请求URL：
 - `http://<domain>/api/sign/history/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

<!--
返回示例:

```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```
-->
返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|		|

备注

 - 更多返回错误代码请看首页的错误代码描述

多要素身份认证接口 (Identity)
------------

简要描述：
 - 多要素身份认证接口

请求URL：
 - `http://<domain>/api/sign/identity/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数：
 - 仅 POST 请求时使用参数

| 参数名			| 必选	| 类型	| 备注						|
| :-- 			| :--: 	| :-- 	|							|
| certId			| √	    | 字符	| 证件号		|
| certType			| x	    | 字符	| 证件类型			|
| name			| √	    | 字符	| 真实姓名		|
| phone			| x	    | 电话	| 银行预留电话		|
| address		| x	    | 字符	| 真实地址			|
| frontPhoto		| √	    | 图片	| 证件照正面		|
| backPhoto | √     | 图片    | 证件照反面     |
| photo	| x	    | 图片	| 上传照片		|
| cardNo | x	    | 字符	| 银行卡号	|
| cvn2 		| x	    | 字符	| 信用卡背面的末3位数字(仅信用卡使用)		|
| level 		| √	    | 字符	| 认证级别 (A, B, C, C)		|


返回示例:

```json
{
    "id": 1,
    "credit": "50",
    "created": "2017-11-08 02:38:20",
    "modified": "2017-11-08 02:38:20",
    "certId": "",
    "certType": 1,
    "name": "",
    "phone": "",
    "originType": 1,
    "address": "",
    "cardNo": "",
    "bankID": "",
    "cvn2": "",
    "dn": "",
    "level": "",
    "serial": "",
    "enddate": ""
}
```

返回参数:

| 参数名			| 类型	| 备注   |
| :-- 			| :--: 	| :-- 	|
| certId			| 字符	| 证件号		|
| certType			| 字符	| 证件类型			|
| name			| 字符	| 姓名		|
| phone			| 电话	| 电话		|
| address		| 字符	| 地址			|
| cardNo | 字符	| 银行卡号	|
| cvn2 		|字符	| 信用卡背面的末3位数字		|
| level 		| 字符	| 认证级别		|
| serial        | 字符    | 证书编号(废弃待定)        |
| dn 		| 字符	| 证书DN		|


备注

 - 更多返回错误代码请看首页的错误代码描述
