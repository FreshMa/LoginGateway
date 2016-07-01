import requests

s = requests.Session()
r = s.get('http://10.3.8.211')
conLen = r.headers['content-length']
iLen = int(conLen)
if iLen<5000:
    requests.get('http://10.3.8.211/F.htm')
    print 'logout!'
else:
    print 'already out'

input()


