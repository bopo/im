银行卡管理
======

> 首次撰写：2017-01-14

> 最后修改：-

接口列表
------------

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/me/bankcard/](#bankcard) | GET / PUT / POST / DELETE|登录用户|银行卡|


银行卡管理 (Bankcard)
------------

简要描述：
 - 银行卡管理

请求URL：
 - `http://<domain>/api/me/bankcard/`

请求方式：
 - `GET` `POST` `PUT` `DELETE`

请求权限：
 - `登录用户`

请求参数：
 - 仅 `POST` `PUT` 请求时使用参数 

| 参数名 | 必选	| 类型	| 备注		|
| :--   | :-- 	| :-- 	|			|
| card  | √	    | 字符	| 银行卡号	|
| bank  | x	    | 字符	| 银行名称	|


返回示例:

```json

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "logo": "http://110.7.7.22:3000/media/banks/default.jpg",
            "cardholder": "张三",
            "bank": "农业银行",
            "card": "6228480402564890018",
            "suff": "0018",
            "type": "金穗通宝卡(银联卡)",
            "flag": ""
        }
    ]
}
```

返回参数:

| 参数名 | 类型 | 备注	|
| :--   | :-- |		|
| logo  | 字符 | 银行LOGO  |
| cardholder  | 字符 | 银行持卡人  |
| card  | 字符 | 银行卡号  |
| bank  | 字符 | 银行名称  |
| type  | 字符 | 卡片类型  |
| flag  | 字符 | 用途标识 (收款，支付等 冗余字段)  |
| suff  | 字符 | 卡片后缀  |

备注
 
 - 更多返回错误代码请看首页的错误代码描述

