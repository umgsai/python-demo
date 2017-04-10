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
import xlrd

data = xlrd.open_workbook('/Users/shangyidong/Downloads/memoData.xlsx')

table = data.sheets()[0] #第一个工作簿
nrows = table.nrows #行数

#path = "http://10.66.40.64:4080/invoke.json"
path = "http://10.1.126.72:4080/invoke.json"

service_url_s = "http://service.***.com/bb/merchant/bill/data/***Service_1.0.0"
method_s = "updateMemoById"

for i in range(nrows):
      id = int(table.row_values(i)[0])
      memo = table.row_values(i)[1].encode("UTF-8")
      #id = 18
      print id
      print memo

      params_s = "parameters[]=%d&parameters[]=%s" % (id, memo)
      params_s += "&url=%s&method=%s&parameterTypes[]=java.lang.Integer&parameterTypes[]=java.lang.String" % (service_url_s, method_s)
      url_s = path + "?" + quote(params_s, safe='&=')

      #print params_s
      #print url_s
      data_s = urllib2.urlopen(url_s).read()
      print json.loads(data_s)
      #break



