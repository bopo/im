朋友圈接口
========


> 首次撰写：2017-11-14

> 最后修改：-

### 接口列表

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
|[/api/timeline/background/](http://10.7.7.22:3000/api/timeline/background/)|GET、POST|登录用户|朋友圈背景图片|
|[/api/timeline/background/?id={pk}](http://10.7.7.22:3000/api/timeline/background/)|GET|登录用户|指定用户朋友圈背景图片 Pk:用户id|
|[/api/timeline/discuss/](http://10.7.7.22:3000/api/timeline/discuss/)|POST|登录用户|发朋友圈|
|[/api/timeline/discuss/{pk}/reply/](http://10.7.7.22:3000/api/timeline/discuss/{pk}/reply/)|POST|登录用户|评论接口，PK：朋友圈id|
|[/api/timeline/discuss/{pk}/praise/](http://10.7.7.22:3000/api/timeline/discuss/{pk}/praise/)|POST|登录用户|点赞接口，PK：朋友圈id|
|[/api/timeline/discuss/{pk}/reward/](http://10.7.7.22:3000/api/timeline/discuss/{pk}/reward/)|POST|登录用户|打赏接口，PK：朋友圈id|
|[/api/timeline/discuss/{pk}/copy/](http://10.7.7.22:3000/api/timeline/discuss/{pk}/copy/)|POST|登录用户|转载，PK：朋友圈id|
|[/api/timeline/discuss/photo/](http://10.7.7.22:3000/api/timeline/photo/)|GET|登录用户|朋友圈相册list|
|[/api/timeline/discuss/photo/query/](http://10.7.7.22:3000/api/timeline/photo/query)|POST|登录用户|指定用户朋友圈相册list|
|[/api/timeline/circle/](http://10.7.7.22:3000/api/timeline/circle/)|POST|登录用户|朋友圈list（我的朋友圈），该接口为查询接口，返回朋友圈消息集合|


背景图接口
-----

简要描述：
 - 朋友圈背景

请求URL：
 - `http://<domain>/api/timeline/background/`

请求方式：
 - `GET,POST`

请求权限：
 - `登录用户`

请求参数：

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|:-- 	|
| background	| Img	| 图片	|


返回参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	 :-- 	|
| nick		| String	| 昵称	|
| avatar		| String	| 头像	|
| background| String	| 背景	|


返回示例：

```


{
    "nick": "",
    "avatar": "avatar/default.jpg",
    "background": null
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述



发朋友圈接口
-----

简要描述：
 - 发一条朋友圈

请求URL：
 - `http://<domain>/api/timeline/discuss/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:--	|
| content			| String	| 文字内容	|
| img			| image	| 图片内容|
| site			| String	| 地址 可空|
| see			| String	| 格式:"1,2,3,4" 用户id用,隔开|
| black			| String	| 格式:"1,2,3,4"，不能和see共同存在|
| remind			| String	| 格式:"1,2,3,4"|
| reprint			| Boolean	| 是否转载 默认false|
| by			| int	| 被转载者id 可空，当转载为true时此项必须有值|



返回示例：

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 122,//话题id
            "nick": "",//用户昵称
            "user_id": "1",//用户id
            "level": "",//用户等级
            "reply": [],//评论
            "praise": [],//点赞
            "reward": [],//打赏
            "created": "2017-11-16 02:35:42",
            "modified": "2017-11-16 02:35:42",
            "content": "text",
            "img": null,
            "site": "北京",
            "see": null,//谁可以看
            "black": null,//谁不可以看
            "remind": null,//提醒谁看
            "reprint":false//是否转载
            "replys": 0,//评论数
            "praises": 0,//点赞数
            "rewards": 0,//打赏数
            "by": null//被转载者id
        }
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述



评论接口
----

简要描述：
 - 评论朋友圈

请求URL：
 - `http://<domain>/api/timeline/discuss/{pk}/reply/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
| text			| String	| 文字内容	|
| incept	| INT	| 被评论者id 默认为朋友圈所属人	|



返回示例：

```

{
    "detail": "成功"
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述


 点赞接口
-----

简要描述：
 - 给朋友圈点赞

请求URL：
 - `http://<domain>/api/timeline/discuss/{pk}/praise/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
| status	| Boolean	| 默认True点赞	|



返回示例：

```

{
    "detail": "成功"
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述


  打赏接口
------

简要描述：
 - 给朋友圈某条打赏

请求URL：
 - `http://<domain>/api/timeline/discuss/{pk}/reward/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
| money	| DecimalField	| 打赏金额	|



返回示例：

```

{
    "detail": "成功"
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述

   转载
-----

简要描述：
 - 转载某条朋友圈

请求URL：
 - `http://<domain>/api/timeline/discuss/{pk}/copy/`

请求方式：
 - `POST`

请求权限：
 - `登录用户`

请求参数:

无



返回示例：

```

{
    "detail": "成功"
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述



 相册接口
-----

简要描述：
 - 朋友圈相册

请求URL：
 - `http://<domain>/api/timeline/photo/query`

请求方式：
 - `GET`

请求权限：
 - `登录用户`

请求参数:

| 参数名			| 类型	| 备注	|
| :-- 			| :-- 	|	:-- 	|
| id	| Int	| 用户id	|



返回示例：

```

{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 16,
            "nick": "",
            "user_id": "2",
            "avatar": "http://10.7.7.170:8000/media/avatar/default.jpg",
            "created": "2017-12-19 01:10:42",
            "modified": "2017-12-19 01:11:40",
            "content": "134",
            "img1": "http://10.7.7.170:8000/media/WechatIMG29.jpeg",
            "img2": null,
            "img3": null,
            "img4": null,
            "img5": null,
            "img6": null,
            "img7": null,
            "img8": null,
            "img9": null,
            "site": null,
            "remind": null,
            "reprint": false,
            "replys": 1,
            "praises": 0,
            "rewards": 1,
            "images": 0,
            "by": null,
            "reprint_type": 0
        }
     ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述




  朋友圈list查询接口
-------------

简要描述：
 - 我的朋友圈list显示信息

请求URL：
 - `http://<domain>/api/timeline/circle/`

请求方式：
 - `GET ，POST`

请求权限：
 - `登录用户`

请求参数:

{ 无 }



返回示例：

```

{
    "count": 9,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 172,
            "owner": "",//所有者
            "owner_id": "1",
            "owner_level": "",
            "acceptor": "",//接收者
            "acceptor_id": "1",
            "acceptor_level": "",
            "by": null, //被转载者
            "by_id": null,
            "by_level": null,
            "discuss": {
                "id": 122,//朋友圈id
                "nick": "", //用户昵称
                "user_id": "1",  //用户id
                "level": "",//用户等级
                "avatar": "avatar/default.jpg",//用户头像
                "reply": [
                    {
                        "id": 1,
                        "sender": "",//回复人
                        "sender_avatar": "avatar/default.jpg",//头像
                        "incept": "",//接收者
                        "incept_avatar": "avatar/default.jpg",//头像
                        "created": "2017-12-11 00:57:16",
                        "modified": "2017-12-11 00:57:16",
                        "text": "111"//内容
                    },
                ],
                "praise": [
                    {
                        "id": 1,
                        "nick": "",//点赞者昵称
                        "avatar": "avatar/default.jpg",//头像
                        "created": "2017-12-11 00:51:00",
                        "modified": "2017-12-11 00:51:00",
                        "status": true,//状态（点赞）
                        "sender": 1,
                        "discuss": 1
                    }
                ],
                "reward": [
                    {
                        "id": 11,
                        "nick": "",//昵称
                        "avatar": "avatar/default.jpg",//头像
                        "created": "2017-11-16 03:24:16",
                        "modified": "2017-11-16 03:24:16",
                        "money": "200.00",//金额
                        "discuss": 122
                    }
                ],
                "created": "2017-11-16 02:35:42",
                "modified": "2017-11-16 02:35:42",
                "content": "111",
                "img": null,
                "replys": 2,
                "praises": 1,
                "rewards": 1,
                "reprint_type":0 //转载格式（0：免费，1：付费，2：禁止，默认：0）
            },
            "created": "2017-11-16 02:35:42",
            "modified": "2017-11-16 02:35:42"
        }
    ]
}

```

备注

 - 更多返回错误代码请看首页的错误代码描述