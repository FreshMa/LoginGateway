# LoginGateway
+ 自动登录、登出校园网网关小脚本，可以查看流量使用情况
+ 支持宿舍和图书馆两种网关，只需要修改login和logout文件中的网关地址即可

## 网关如下：
+ 宿舍         http://10.3.8.211   
+ 图书馆、教室 http://10.4.1.2     

## 核心代码就几句：
+ 登录：
    import requests
    gateAdd = 'http://10.3.8.211'
    #图书馆等
    #gateAdd = 'http://10.4.1.2'
    login_form={'DDDDD':'帐号','upass':'密码','0MKKey':''}
    s.post(gateAdd,login_form)
+ 登出：
    import requests
    gateAdd = 'http://10.3.8.211'
    #图书馆等
    #gateAdd = 'http://10.4.1.2'
    suf = '/F.htm'
    requests.get(gateAdd+suf)
