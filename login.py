
# -*-coding:utf-8 -*-

from decimal import *
from bs4 import BeautifulSoup
import lxml
import requests
import re
import time


s = requests.Session()
#宿舍、图书馆网关均可，改一下网关地址即可
gateAdd = 'http://10.3.8.211'
#gateAdd = 'http://10.4.1.2'
def login():
    st = checkOnline2()
    #需要输入自己的帐号和密码
    login_form={'DDDDD':'帐号','upass':'密码','0MKKey':''}
    if st == 'out': 
        s.post(gateAdd,login_form)
        print u'登录成功，帐号为 %s'%login_form['DDDDD']
        displayInfo()
    else:
        print u'已处于登录状态，帐号为 %s'%login_form['DDDDD']
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

#分钟 -> 小时+分钟
def parseTime(time):
    minute = time%60
    hour = time/60
    return hour,minute

def displayInfo():
    r = s.get(gateAdd)
    html = r.text
    #使用BeautifulSoup来提取网页中的javascript脚本
    soup = BeautifulSoup(html,'lxml')
    #只需要script列表中第一个就行
    script = soup.find_all('script')[0].string
    #将该script脚本分行切割，发现第二行包含了我们需要的使用情况信息，故保存
    infoStr = script.splitlines()[1]
    #使用正则匹配出使用时间以及流量等信息，开头.*为了匹配10.4.1.2
    m = re.match(r'^.*time=\'(\d*)\s*\';flow=\'(\d*)\s*\'.*fee=\'(\d*)\s*\'.*',infoStr)
    time = m.group(1)
    flow = int(m.group(2))
    fee = int(m.group(3))
    
    #时间tuple
    timeT = parseTime(time)
    hour = timeT[0]
    minute = timeT[1]

    #余额
    fee1 = (float)(fee-fee%100)/10000
    
    #根据js中的计算方法计算流量，将byte转为Mbyte
    flow0 = flow%1024
    flow1 = flow-flow0
    flow0 = flow0*1000
    flow0 = flow0-flow0%1024
    #整数部分
    flow1 = flow1/1024
    #小数部分
    flow0 = flow0/1024
    #将近多少GB
    flow3 = round((Decimal(flow1)/Decimal(1024)),2)

    #拼接流量字符串
    flow1Str = str(flow1)
    flow0Str = str(flow0)
    flowStr = flow1Str+'.'+flow0Str
    
    flowInfo = u'使用流量: %+9s MB，将近%4.2fGB'%(flowStr,flow3)
    timeInfo = u'使用时间: %3d小时%3d分钟'%(hour,minute)
    feeInfo = u'余额: %9.2f 元'%fee1

    print timeInfo
    print flowInfo
    print feeInfo
    
login()
#命令行界面延迟一秒消失
time.sleep(1)
