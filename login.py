import requests

s = requests.Session()
def login():
    st = check()
    if st == 'out':
        login_form={'DDDDD':'2011212063','upass':'286036','0MKKey':''}
        s.post('http://10.3.8.211',login_form)
        print 'login successfully, the account is %s'%login_form['DDDDD']
        print
    else:
        print 'already login,the account is %s'%login_form['DDDDD']

def check():
    r = s.get('http://10.3.8.211')
    conLen = r.headers['content-length']
    iLen = int(conLen)
    if iLen<5000:
        status = 'on'
    else:
        status = 'out'
    return status

login()
input()
