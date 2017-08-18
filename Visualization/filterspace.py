# encoding = utf-8 #

# 过滤掉数据txt中的空格

import re

ifn = r"in.txt"
ofn = r"data.csv"

infile = open(ifn,'r')
outfile = open(ofn,'w')

i = 0

for eachline in infile.readlines():
    # lines = eachline.split(' ')
    lines = re.sub(', ',',',eachline)   # 将", " 替换成 "," 这样在处理数据的时候才方便读入成一个int 而不是string
    outfile.write(lines)
    i += 1
    print(i)
