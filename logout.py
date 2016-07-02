import requests
import time

def logout():
    s = requests.Session()
    r = s.get('http://10.3.8.211')
    conLen = r.headers['content-length']
    iLen = int(conLen)
    if iLen<5000:
        requests.get('http://10.3.8.211/F.htm')
        print 'logout successfully!'
    else:
        print 'already out'

logout()
time.sleep(1)
