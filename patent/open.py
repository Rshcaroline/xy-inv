# -*- coding:utf-8 -*-

import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# csv.field_size_limit(922337203)
with open('index.txt') as f:
# f = open(root+'zhidao4.csv')
    cv = f.readlines()
    for line in cv:
        line = line.replace(u'\\', '/')
        print line
        time.sleep(3)
    f.close()
print 'done'