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

data = xlrd.open_workbook('/Users/shangyidong/Downloads/6e5e4576d2a24801afcd0470fbe0e7ce.xlsx')

table = data.sheets()[0] #第一个工作簿

nrows = table.nrows #行数

#print nrows

ncols = table.ncols #列数

#print ncols

f=file('/Users/shangyidong/Downloads/MemoData.txt','a')

path = "http://10.66.40.64:4080/invoke.json"
service_url_s = "http://service.dianping.com/bb/merchant/bill/data/BillDailyFlowService_1.0.0"
method_s = "updateMemoById"

for i in range(nrows):
      id = int(table.row_values(i)[0])
      #print (table.row_values(i)[22]).encode("UTF-8")
      memo = "营销结算-扣款|" + (table.row_values(i)[2]).encode("UTF-8").split("营销结算-扣款|")[1]

      print id
      print memo
      f.write(str(id))
      f.write("\t")
      f.write(memo)
      f.write("\n")
      #id = 14

      #params_s = "parameters[]=%d&parameters[]=%s" % (id, memo)
      #params_s += "&url=%s&method=%s&parameterTypes[]=java.lang.Integer&parameterTypes[]=java.lang.String" % (service_url_s, method_s)
      #url_s = path + "?" + quote(params_s, safe='&=')

      #print params_s
      #print url_s
      #data_s = urllib2.urlopen(url_s).read()
      #print json.loads(data_s)
      #f.write(str(id) + '\t')
      #f.write(memo + '\n')
      #print table.row_values(i)
      #break


