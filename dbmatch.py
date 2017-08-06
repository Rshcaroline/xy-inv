# -*- coding:utf-8 -*-

# 匹配申请人

# import pandas as pd
import numpy as np
import re
import csv
import sys
import time
# import levenshtein

reload(sys)
sys.setdefaultencoding('utf-8')


def write(r):
    outfile = open('dbapcp.csv', 'ab')
    writer = csv.writer(outfile)
    writer.writerow(r)
    outfile.close()
    return 0

if __name__ == '__main__':

    # applicant = csv.reader(open('CN-BIBS-ABSS-10-A_20170315.csv','rb'))
    applicant = csv.reader(open('test2.csv', 'rb'))
    cp = csv.reader(open('test.csv','rb'))
    counts = []
    cps = []
    for row_cp in cp:
        cps.append(row_cp)
        counts.append(0)
    print len(cps)

    for row_ap in applicant:
        # cp = csv.reader(open('Company.csv', 'rb'))
        # cp = csv.reader(open('test.csv', 'rb'))
        a = row_ap[0]
        for i in range(len(cps)):
            c = cps[i][0].replace('.\\', '')
        # applicant = csv.reader(open('test2.csv', 'rb'))
            # write([row_ap[5], row_cp])
            # arith = levenshtein.arithmetic()
            # print arith.levenshtein(row_ap[5].encode('utf-8'), row_cp[3].encode('utf-8'))
            # result = re.findall(row_cp[3], row_ap[5])
            result = re.findall(c, a)
            if len(result) > 0:
                counts[i] = counts[i] + 1
                break
        print a
    for i in range(len(counts)):
        print i
        write([cps[i], counts[i]])
