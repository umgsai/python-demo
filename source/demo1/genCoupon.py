#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com
# Created Time: 2017-02-10 10:59:45

import sys
import random

for i in xrange(0, int(sys.argv[1])):
    coupon = ''
    for j in xrange(0, 10):
        coupon += str(random.randint(0, 9))
    print coupon

