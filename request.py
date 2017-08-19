#!/usr/bin/env python

import requests
url = 'http://news.163.com'
response = requests.get(url)
print response.status_code
