商城部分
======

> 首次撰写：2017-11-14

> 最后修改：-

接口列表
------------

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/mall/address/](#address) | GET |登录用户|用户地址列表|
| [/api/mall/orders/](#orders) | GET |登录用户|订单列表|
| [/api/mall/favorite/](#favorite) | GET |登录用户|商品关注列表|
| [/api/mall/footprint/](#footprint) | GET |登录用户|商品浏览足迹|
| [/api/mall/sendmall/](#sendmall) | GET |登录用户|发送邮件|


订单列表
-----


简要描述：
 - 军队电商订单，发票信息 查询

请求URL：
 - `http://<domain>/api/mall/orders/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- |
|page   |string |第几页   |
|sizepage     |string | 一页查询几条    |
|order_sn     |string | 订单号搜索    |


返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|order_id  |int   |自增ID |
|order_sn  |varchar   | 订单号,唯一 |
|inv_payee   |varchar   |发票抬头,用户页面填写 |
|inv_content   |varchar   |	发票内容,用户页面选择 |
|user_id   |mediumint   |	用户id,同users的user_id |
|surplus  |int   |该订单使用金额的数量,取用户设定余额,用户可用余额,订单金额中最小者 |
|order_status  |int   |订单的状态;0未确认,1确认,2已取消,3无效,4退货 |
|shipping_status  |int   |商品配送情况;0未发货,1已发货,2已收货,4退货 |
|pay_status  |int   |支付状态;0未付款;1付款中;2已付款 |
|pay_time  |int   |订单支付时间 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results":  [
        {
            "order_id": 49,
            "order_sn": "2017112710354330193",
            "surplus": "7815.00",
            "order_status": 5,
            "shipping_status": 2,
            "pay_status": 2,
            "pay_time": 1511721324,
            "inv_payee": "发票抬头",
            "inv_content": "办公用品"
        },
        {
            "order_id": 48,
            "order_sn": "2017112710246611861",
            "surplus": "24.00",
            "order_status": 1,
            "shipping_status": 0,
            "pay_status": 2,
            "pay_time": 1511720174,
            "inv_payee": "发票抬头",
            "inv_content": "办公用品"
        },
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述







 用户地址列表
-----


简要描述：
 - 用户收货地址

请求URL：
 - `http://<domain>/api/mall/address/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- |
|page   |string |第几页   |
|sizepage     |string | 一页查询几条    |


返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|address_id  |int   |收货信息id |
|address_name  |varchar   | 名字 |
|consignee  |varchar   | 收货人 |
|user_id   |mediumint   |	用户id,同users的user_id |
|country  |int   |国家|
|province  |int   |省份 |
|city  |int   |城市 |
|district  |int   |区 |
|address  |varchar   |详细地址 |
|mobile  |varchar   |手机号 |
|best_time  |varchar  |收货人的最佳收货时间 |
|zipcode  |varchar  |收货人的邮编 |
|sign_building  |varchar  |收货人标志性建筑 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results":  [

        {
            "address_id": 51,
            "address_name": "",
            "user_id": 126,
            "consignee": "收货人",
            "country": "中国",
            "province": "北京",
            "city": "北京",
            "district": "东城区",
            "street": 0,
            "address": "详细信息",
            "zipcode": "",
            "tel": "",
            "mobile": "13146114608",
            "sign_building": "",
            "best_time": "",
            "audit": 0
        }
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述





商品关注列表
-----


简要描述：
 - 商品收藏 关注查询

请求URL：
 - `http://<domain>/api/mall/favorite/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- |
|page   |string |第几页   |
|sizepage     |string | 一页查询几条    |


返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|rec_id |mediumint   |收藏记录的自增id  |
|goods_id |mediumint   |收藏的商品id，取值于goods的goods_id  |
|add_time |int   |收藏时间  |
|is_attention |tinyint   |是否关注该收藏商品;1是;0否 |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results":  [
        {
            "rec_id": 50,
            "goods_id": 792,
            "add_time": 1511489218,
            "is_attention": 0
        }
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述




 商品浏览足迹
-----


简要描述：
 - 商品收藏 关注查询

请求URL：
 - `http://<domain>/api/mall/footprint/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：



| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- |
|page   |string |第几页   |
|sizepage     |string | 一页查询几条    |


返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
|goods_id |int   |商品id |
|goods_name |va   |商品名字 |
|shop_price |f   |人民币销售价格 |
|szb_shop_price |f   |数字币价格 |
|goods_thumb |va   |图片地址 调用的时候加上 商城 主域名（暂时先这样测试后期要修改） |


返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results":  [
        {
            "goods_id": 916,
            "goods_name": "liuli",
            "shop_price": "130.00",
            "goods_thumb": "images/201711/thumb_img/0_thumb_G_1510190909853.jpg",
            "szb_shop_price": "115.00"
        }
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述

 发送邮件
-----


简要描述：
 - 发送邮件

请求URL：
 - `http://<domain>/api/mall/sendmall/`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数：


| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- |
|id   |string |合约ID   |
|email     |string | 收件人邮箱地址    |


备注

 - 更多返回错误代码请看首页的错误代码描述