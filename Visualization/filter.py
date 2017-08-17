#encoding = utf-8#

#过滤掉数据txt中的空格

import os, sys, string

ifn = r"data.csv"
ofn = r"Output.txt"

infile = open(ifn,'rb')
outfile = open(ofn,'wb')

for eachline in infile.readlines():
    lines = eachline.split(', ')
    for temp in lines:
        print(temp)
        outfile.write(temp+'\n')

infile.close
outfile.close