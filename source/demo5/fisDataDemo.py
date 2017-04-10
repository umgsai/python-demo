#!/usr/bin/env python
# coding=utf-8
# Author: shangyidong
# Mail: shangyidong@meituan.com
import os
import sys
import time
import json
import urllib
import urllib2
from urllib import quote


path = "http://10.1.121.291:4080/invoke.json"

service_url_s = "http://service.***.com/***/**Service_1.0.0"
method_s = "manualAuditSR"
#payplanid = 139305539
voucherId = 115213
result = 1
params_s = "parameters[]=%d&parameters[]=%d" % (voucherId, result)
params_s += "&url=%s&method=%s&parameterTypes[]=int&parameterTypes[]=int" % (service_url_s, method_s)
url_s = path + "?" + quote(params_s, safe='&=')

print params_s
print url_s
data_s = urllib2.urlopen(url_s).read()
print json.loads(data_s)



