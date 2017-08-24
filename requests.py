#!/usr/bin/env python

import urllib2

request = urllib2.Request('http://httpbin.org/get')

request.add_data('a','1')
request.add_header('User-Agent','Mozilla/5.0')

response = urllib2.urlopen(request)
