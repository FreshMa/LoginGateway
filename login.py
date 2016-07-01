import requests

s = requests.Session()
gateAdd = 'http://10.3.8.211'
def login():
    st = check()
     #需要输入自己的帐号和密码
    login_form={'DDDDD':'上网账号','upass':'上网密码','0MKKey':''}
    if st == 'out':
        s.post(gateAdd,login_form)
        print 'login successfully, the account is %s'%login_form['DDDDD']
    else:
        print 'already login,the account is %s'%login_form['DDDDD']

def check():
    #检测是否处于登录状态，抓包发现未登录前header的content-length属性的值大于5000，登录之后小于5000，故据此来判断
    r = s.get(gateAdd)
    conLen = r.headers['content-length']
    iLen = int(conLen)
    if iLen<5000:
        status = 'on'
    else:
        status = 'out'
    return status

login()
input()
