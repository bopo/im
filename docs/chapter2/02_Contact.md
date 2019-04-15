通讯录部分
======

> 首次撰写：2017-11-14

> 最后修改：-

接口列表
------------
> - 通讯录有三种状态 `invite`， `confirm` 和 `done` 
> - 一个用户邀请另外一个用户，邀请方的通讯录里对方的状态是 invite，被邀请方的状态 confirm， 被邀请方确定以后 两个用户状态都为 done，也就是完成状态 

|接口|方法|权限|备注|
| :-- | :-- | :-- | :-- |
| [/api/me/contact/](#contact) | GET / POST | 登录用户 |通讯录列表|
| [/api/me/contact/[id]/](#contact_detail) | GET / PUT / DELETE|登录用户 | 获取好友信息(GET) <br />设置黑名单隐藏(PUT)<br />删除好友(DELETE) |
| [/api/me/contact/black/](#contact_black) | PUT | 登录用户 |批量隐藏我名字(批量)|
| [/api/me/contact/hide/](#contact_hide) | PUT | 登录用户 | 批量隐藏我名字 <br /> `userid` 参数 多个用户用英文逗号分隔，<br />例如 1,2,3,4,5 |
| [/api/me/contact/black/](#contact_black_batch) | PUT | 登录用户 | 批量黑名单 <br /> `userid` 参数 多个用户用英文逗号分隔，<br />例如 1,2,3,4,5 |
| [/api/me/contact/circle_hid/]() | PUT | 登录用户 | 批量朋友圈不可见 <br /> `userid` 参数 多个用户用英文逗号分隔，<br />例如 1,2,3,4,5 |
| [/api/me/contact/circle_show/]() | PUT | 登录用户 | 批量朋友圈可见 <br /> `userid` 参数 多个用户用英文逗号分隔，<br />例如 1,2,3,4,5 |
| [/api/me/contact/blacklist/](#contact_black_batch) | GET | 登录用户 | 黑名单列表 |
| [/api/me/contact/hidcirclelist/]() | GET | 登录用户 | 朋友圈不可见list |

