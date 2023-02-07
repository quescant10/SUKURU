import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'www.google.com')
