#!/usr/bin/env python
# coding=utf-8
# Author: shangyidong
# Mail: shangyidong@meituan.com
import xlrd

data = xlrd.open_workbook('/Users/shangyidong/Downloads/201703综合预定.xlsx')

table = data.sheets()[1] #第一个工作簿
nrows = table.nrows #行数
f = open('/Users/shangyidong/Downloads/test.txt', 'r+')
f.truncate()
for i in range(nrows):
      bizid = table.row_values(i)[7]
      bizid = bizid.strip('\n')
      print "'" + bizid + "',"
      f.write("'" + bizid + "'," + "\n")
      #print len(bizid)
      #print i