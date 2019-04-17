module github.com/bopo/im

go 1.12

require (
	github.com/bitly/go-simplejson v0.5.0
	github.com/bmizerany/assert v0.0.0-20160611221934-b7ed37b82869 // indirect
	github.com/go-sql-driver/mysql v1.4.1
	github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b
	github.com/golang/protobuf v1.3.0
	github.com/gomodule/redigo v2.0.0+incompatible
	github.com/googollee/go-engine.io v0.0.0-20180611083002-3c3145340e67
	github.com/gorilla/websocket v1.4.0
	github.com/importcjj/sensitive v0.0.0-20190124053339-62a4c32ecfda
	github.com/kr/pretty v0.1.0 // indirect
	github.com/richmonkey/cfg v0.0.0-20130815005846-4b1e3c1869d4
	github.com/smartystreets/goconvey v0.0.0-20190330032615-68dc04aab96a // indirect
	github.com/valyala/gorpc v0.0.0-20160519171614-908281bef774
	golang.org/x/net v0.0.0-20180906233101-161cd47e91fd
	google.golang.org/grpc v0.0.0-00010101000000-000000000000
)

replace (
	cloud.google.com/go => github.com/googleapis/google-cloud-go v0.26.0
	golang.org/x/lint => github.com/golang/lint v0.0.0-20180702182130-06c8688daad7
	golang.org/x/net => github.com/golang/net v0.0.0-20181011144130-49bb7cea24b1
	golang.org/x/oauth2 => github.com/golang/oauth2 v0.0.0-20180821212333-d2e6202438be
	golang.org/x/sync => github.com/golang/sync v0.0.0-20180314180146-1d60e4601c6f
	golang.org/x/sys => github.com/golang/sys v0.0.0-20180830151530-49385e6e1522
	golang.org/x/text => github.com/golang/text v0.3.0
	golang.org/x/tools => github.com/golang/tools v0.0.0-20180828015842-6cd1fcedba52
	google.golang.org/appengine => github.com/golang/appengine v1.1.0
	google.golang.org/genproto => github.com/google/go-genproto v0.0.0-20180817151627-c66870c02cf8
	google.golang.org/grpc => github.com/grpc/grpc-go v1.16.0
)
