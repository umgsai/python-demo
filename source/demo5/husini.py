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
import Image

import httplib
conn = httplib.HTTPConnection("service.sh.189.cn")
conn.request("GET", "/service/createValidate.do?key=validateName&time=0.8945831979292289")
r1 = conn.getresponse().read()
print r1
