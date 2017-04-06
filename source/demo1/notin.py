#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com

import sys

left = set(x[:-1] for x in open(sys.argv[1]).xreadlines())
right = set(x[:-1] for x in open(sys.argv[2]).xreadlines())

for item in left - right:
    print item

