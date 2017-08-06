# -*- coding:utf-8 -*-

# 匹配申请人

# import pandas as pd
import numpy as np
import re
import csv
import sys
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

    applicant = csv.reader(open('CN-BIBS-ABSS-10-A_20170315.csv','rb'))
    # cp = csv.reader(open('Company.csv','rb'))

    for row_ap in applicant:
        cp = csv.reader(open('Company.csv','rb'))
        for row_cp in cp:
            str1 = row_ap[5]
            str2 = row_cp[3]
            # print str1, str2
            re.findall('万科', str1)
            # write([row_ap[5], row_cp])
            # arith = levenshtein.arithmetic()
            # print arith.levenshtein(row_ap[5].encode('utf-8'), row_cp[3].encode('utf-8'))
            # re.findall(row_ap[5].encode('utf-8'), row_cp[3].encode('utf-8'))
            # print row_ap[5].encode('utf-8'), row_cp[3].encode('utf-8')
