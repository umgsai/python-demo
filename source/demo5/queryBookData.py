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
import xlrd

data = xlrd.open_workbook('/Users/shangyidong/Downloads/201702综合预订1.xlsx')

table = data.sheets()[0] #第一个工作簿
nrows = table.nrows #行数
ncols = table.ncols #列数
print nrows
f=file('/Users/shangyidong/Downloads/data.txt','a')
for i in range(nrows):
    tmp = ""
    for j in range(int(ncols)):
        tmp += str(table.row_values(i)[j]).replace("\n", "")
        tmp = tmp + ","
    print tmp
    f.write(tmp + "\n")
        #f.write(str(table.row_values(i)[0]) + "\t" + table.row_values(i)[1] + "\t" + table.row_values(i)[2] + "\t" + table.row_values(i)[3] + "\t" + table.row_values(i)[4] + "\t" + table.row_values(i)[0])
      #print "\"" + table.row_values(i)[5] + "\","
      #print table.row_values(i)[j]
    #if i == 2:
     #   break