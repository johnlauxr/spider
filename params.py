#!/usr/bin/env python

import requests

url = 'http://httpbin.org/get'
payload = {'key1':'value1','key2':'value2'}
r = requests.get(url,params=payload)
print r.url


