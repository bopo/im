消息中心
======

> 首次撰写：2017-11-14

> 最后修改：-

用户消息中心 (Notices)
------------

简要描述：

- 用户消息中心

请求URL：

- `http://<domain>/api/me/notices/`

请求方式：

- `PUT` `GET`

请求权限：

- `登录用户`

请求参数：

- 仅 PUT 请求时使用参数 


返回示例:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "subject": "稍等是",
            "content": "",
            "extra": "",
            "type": ""
        },
        {
            "id": 2,
            "subject": "稍等是2",
            "content": "",
            "extra": "",
            "type": ""
        }
    ]
}
```

返回参数:

| 参数名 | 类型 | 备注 |
| :--- | :--- | --- |
| subject | 字符  | 消息主题 |
| content | 字符  | 消息正文 |
| extra   | 字符  | 附加内容 |
| type    | 字符  | 消息类型 |

备注
 
 - 更多返回错误代码请看首页的错误代码描述


