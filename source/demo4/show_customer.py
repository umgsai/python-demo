#!/usr/bin/env python
# coding=utf-8
# Author: bostin.wang
# Mail: bostinwangbo@gmail.com
# Created Time: 2016-07-30 15:16:32

import sys
import json

from customer import getCustomerInfo

reload(sys)
sys.setdefaultencoding('utf-8')

bean = getCustomerInfo(sys.argv[1])
print json.dumps(bean, indent=4, ensure_ascii=False)
