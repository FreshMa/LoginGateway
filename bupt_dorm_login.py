#-*-coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import time

def login(url,data):
    requests.post(url,data = data)

def logout(url):
    requests.get(url)

def check():
    url = 'http://10.3.8.211'
    r = requests.get(url)
    ht = r.text
    soup = BeautifulSoup(ht,'lxml')
    ti = soup.title.string
    out_s = u'上网注销窗'
    if cmp(ti,out_s)==0:
        return 1
    else:
        return 0
        

def main():
    login_url = "http://10.3.8.211"
    logout_url = 'http://10.3.8.211/F.htm'

    if check():
        op = raw_input(unicode('已登录，要登出吗? y/n : ','utf-8').encode('gbk')).strip()
        #time.sleep(3)
        if(op=='y' or op=='Y'):
            logout(logout_url)
            return 1
        else:
            return 1
            
    else:
        acc = raw_input(unicode('输入账号:','utf-8').encode('gbk')).strip()
        pwd = raw_input(unicode('输入密码:','utf-8').encode('gbk')).strip()
        data = {'DDDDD':acc,'upass':pwd,'0MKKey':''}
        login(login_url,data)
        while(1):
            if(check()==1):
                print u'登录成功'
                return 1
            else:
                print u'登录失败，请检查账号密码或网络'
                return 0
if __name__=='__main__':
    while(1):
        if(main()):
            break
    #raw_input()

