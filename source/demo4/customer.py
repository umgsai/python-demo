#! /usr/bin/env python
# coding=utf-8
######################################################################
# Author: bostin.wang@dianping.com
# Create Time: 2016-07-05 16:28:42
# Descriptioin:
######################################################################

import json
import sys
import urllib2
from urllib import quote

reload(sys)
sys.setdefaultencoding('utf-8')


def getCustomerInfo(customerId):

    path = "http://10.1.117.21:4080/invoke.json"
    service_url = "http://service.dianping.com/customerInfoService/customerInfoService_1.0.0"
    method = "getCustomer"

    params = '''parameters[]=%s&parameters[]=-1''' %(customerId)
    params += '''&url=%s&method=%s&parameterTypes[]=int&parameterTypes[]=int''' %(service_url, method)
    url = path + "?" + quote(params, safe='&=')
    data = urllib2.urlopen(url).read()
    bean = json.loads(data)
    return bean

if __name__ == '__main__':
    for customerId in [x.strip().split()[0] for x in open(sys.argv[1]).xreadlines()]:

        customerName = ''
        contactName = ''
        contactPhone = ''
        bank_province = ''
        bank_city = ''

        try:
            bean = getCustomerInfo(customerId)
            customerName = bean['customerName']
            contactName = bean['contacts'][0]['contactName']
            contactPhone = bean['contacts'][0]['contactMobile']
            bank_province = bean['bankAccounts'][0]['province']
            bank_city = bean['bankAccounts'][0]['city']
        except:
            pass

        print customerId+"\t"+customerName+"\t"+contactName+"\t"+contactPhone+"\t"+bank_province+"\t"+bank_city
