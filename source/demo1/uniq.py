#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com

import sys

for line in set(x.strip() for x in open(sys.argv[1]).xreadlines()):
    print line
