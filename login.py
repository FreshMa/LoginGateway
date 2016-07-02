
# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import lxml
import requests
import re
import time

s = requests.Session()
#宿舍网关，该脚本只考虑了这种情况，在图书馆或者教室的网关不一样，所以就不能使用了
gateAdd = 'http://10.3.8.211'
def login():
    st = checkOnline2()
    #需要输入自己的帐号和密码
    login_form={'DDDDD':'上网账号','upass':'上网密码','0MKKey':''}
    if st == 'out': 
        s.post(gateAdd,login_form)
        displayInfo()
        print 'login, the account is %s'%login_form['DDDDD']
    else:
        print 'already login,the account is %s'%login_form['DDDDD']
        displayInfo()

 #检测是否处于登录状态，抓包发现未登录前header的content-length属性的值大于5000，登录之后小于5000，故据此来判断
def checkOnline():
    r = s.get(gateAdd)
    conLen = r.headers['content-length']
    iLen = int(conLen)
    if iLen<5000:
        status = 'on'
    else:
        status = 'out'
    return status

#检测是否处于登录状态，通过网页的title来判断，更加准确
def checkOnline2():
    r = s.get(gateAdd)
    #防止中文网页乱码
    r.encoding = 'GBK'
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    title = soup.title.string
    logStr = u'上网注销窗'
    if cmp(title,logStr):
        status = 'out'
    else:
        status = 'on'
    return status

def displayInfo():
    r = s.get(gateAdd)
    html = r.text
    #使用BeautifulSoup来提取网页中的javascript脚本
    soup = BeautifulSoup(html,'lxml')
    #只需要script列表中第一个就行
    script = soup.find_all('script')[0].string
    #将该script脚本分行切割，发现第二行包含了我们需要的使用情况信息，故保存
    infoStr = script.splitlines()[1]
    #使用正则匹配出使用时间以及流量等信息
    m = re.match(r'^time=\'(\d*)\s*\';flow=\'(\d*)\s*\'.*',infoStr)
    time = m.group(1)
    flow = int(m.group(2))
    #根据js中的计算方法计算流量，将byte转为Mbyte
    flow0 = flow%1024
    flow1 = flow-flow0
    flow0 = flow0*1024
    flow0 = flow0-flow0%1024
    #整数部分
    flow1 = flow1/1024
    #小数部分
    flow0 = flow0/1024

    flowStr = 'The used traffic is %d.%d MB'%(flow1,flow0)
    timeStr = 'The used time is %s Min'%time

    print timeStr
    print flowStr
    
login()
#命令行界面延迟一秒消失
time.sleep(1)
