二维码扫描格式定义
===============

> 首次撰写：2017-12-05

> 最后修改：-

二维码内容为一个 json 格式的数据.
数据格式为

```json
{
	type:<type>,
	data:<data> // `data` 内容为 `json` 内容转 `hex`
}
```

> data 内容根据不同接口而变化，具体定义见下表

*** 注: ***
 
 - 所有 `<var>` 标签数据为可变数据
 - 类似 `<('receipt', '收据'), ('borrow', '借条'), ('owe', '欠条')>` 的数据为可变枚举
 

扫描加好友(邀请)
-------------

```json
{
	"type": "invite",
	"data": {
		"url":"/api/users/[id]/invite/"
	}
}
```

合约扫描(借条，欠条)
-----------------
```json
type: contract
data: {
	type:<('receipt', '收据'), ('borrow', '借条'), ('owe', '欠条')>
	status:<('', '无状态'), ('agree', '同意'), ('reject', '拒绝')>
	uri:<uri>,
	id:<id>,
}
```

交易(转账，收款)
-----------------
```json
type: transfer
data: {
	type:<('transfer', '转账'),('receiver', '收款'),('thirty', '第三方')>
	status:<('normal', '无状态'), ('agree', '同意'), ('reject', '拒绝')>
	uri:<uri>,
	id:<id>,
}
```