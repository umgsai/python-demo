#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com
# Created Time: 2017-02-10 14:12:53

import sys

mobile = 0
phoneCompany = 0
shortPhone = 0
other = 0

for phone in set(x[:-1].split()[1] for x in open(sys.argv[1]).xreadlines()):
    if len(phone) == 11 and phone[:2] in ('13', '14', '15', '18', '17'):
        mobile += 1
    elif len(phone) == 10 and any(phone.startswith(x) for x in ('400', '800')):
        phoneCompany += 1
    elif len(phone) == 5:
        shortPhone += 1
    else:
        other += 1

print '------------------'
print mobile
print phoneCompany
print shortPhone
print other
