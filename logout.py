# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def logout():
    gateAdd = 'http://10.3.8.211'
    #gateAdd = 'http://10.4.1.2'
    suf = '/F.htm'
    s = requests.Session()
    r = s.get(gateAdd)
    r.encoding = 'GBK'
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    title = soup.title.string
    logStr = u'上网注销窗'
    if cmp(title,logStr):
        print u'已处于下线状态，不必执行此操作'
    else:
        requests.get(gateAdd+suf)
        print u'下线成功'
        
        
logout()
time.sleep(1)
