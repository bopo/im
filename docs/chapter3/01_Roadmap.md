各种流程图时序图
==========

> 首次撰写：2017-11-14

> 最后修改：-

简单登录流程
----------

<div class="diagram">
participant 手机端
participant 服务器
Note over 手机端: 生成密钥对
手机端->服务器: 发送机器码和公钥
Note over 服务器: 存储公钥生成 uid 和 token
服务器->手机端: 返回 uid 和 token

</div>

电商关联流程
----------

<div class="diagram">
participant 手机端
participant 服务器
participant 电商端
手机端->电商端: 发送 uid 和 token
电商端-->服务器: 验证 uid 和 token
服务器-->电商端: 验证成功
电商端->手机端: 返回成功

</div>

验签服务流程
----------

<div class="diagram">
participant 手机端
participant 服务器
participant 加密端
participant 验签端
手机端->服务器: 提交合约请求
服务器->手机端: 返回代签原文
手机端-->加密端: 签名代签原文
加密端-->手机端: 返回签名密文
手机端->服务器: 发送密文+原文ID
Note over 服务器: 通过原文ID找到原文内容
服务器-->验签端: 发送密文+原文
验签端-->服务器: 验签成功
Note over 服务器: 处理业务
服务器->手机端: 返回成功
</div>

身份认证流程(EID+认证)
----------

<div class="diagram">
participant 手机端
participant 服务器
participant EID服务
Note over 手机端: 用户输入信息
手机端->服务器: 提交用户输入信息
服务器-->EID服务: 提交用户信息(IDcard, name)
Note over EID服务: 验证用户信息
EID服务-->服务器: 返回DN和Token
Note over 服务器: 处理用户信息
服务器->手机端: 返回DN
Note over 手机端: 下载证书
</div>


eID+ 验签流程
----------

<div class="diagram">
participant 手机端
participant 服务器
participant EID验签
Note over 手机端: 用户输入信息
手机端->服务器: 发送验签流水号等
服务器-->EID验签: 提交验签参数以及流水号
Note over EID验签: 完成操作
EID验签-->服务器: 返回提交完成状态
服务器->手机端: 返回手机SDK完成状态
手机端->EID验签: 手机SDK发送进行验签
EID验签-->手机端: 返回提交完成状态
手机端->服务器: 发送验签流水号查询验签状态
服务器-->EID验签: 查询验签状态
EID验签-->服务器: 返回查询状态
Note over 服务器: 更新验签记录
</div>

数字币流程
----------

<div class="diagram">
</div>

数字币支付流程
----------

<div class="diagram">
</div>

用户加好友流程
----------

<div class="diagram">
participant 用户A
participant 用户B
participant 服务器
</div>


合约流转流程
----------

<div class="diagram">
participant 用户A
participant 用户B
participant 服务器

</div>

红包发送流程
----------

<div class="diagram">
participant 用户A
participant 用户B
participant 服务器
</div>

面对面加群流程
----------

<div class="diagram">
</div>