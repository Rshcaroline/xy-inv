# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 15:20
# @Author  : shihan.ran
# @Site    :
# @File    : getdatalist.py
# @Software: PyCharm

'''
该脚本包含了从数据读入 处理去空格 生成js文件及全局变量
并可以直接自动打开浏览器 显示已经生成好的图片
'''

import csv
import json
import webbrowser
import os

os.system('python filterspace.py')

reader = csv.reader(open("data.csv"))

sbp = []
sap = []

for contradiction, time, lastprice, volume, bp1, bv1, bp2, bv2, bp3, bv3, bp4, bv4, bp5, bv5, bp6, bv6, \
    bp7, bv7, bp8, bv8, bp9, bv9, bp10, bv10, ap1, av1, ap2, av2, ap3, av3, ap4, av4, ap5, av5, ap6, av6, \
    ap7, av7, ap8, av8, ap9, av9, ap10, av10 in reader:

    if contradiction == 'ag1712':
        b1 = [time,bp1,bv1]
        a1 = [time,ap1,av1]
        sbp.append(b1)
        sap.append(a1)

        b2 = [time,bp2,bv2]
        a2 = [time,ap2,av2]
        sbp.append(b2)
        sap.append(a2)

        b3 = [time,bp3,bv3]
        a3 = [time,ap3,av3]
        sbp.append(b3)
        sap.append(a3)

        b4 = [time,bp4,bv4]
        a4 = [time,ap4,av4]
        sbp.append(b4)
        sap.append(a4)

        b5 = [time,bp5,bv5]
        a5 = [time,ap5,av5]
        sbp.append(b5)
        sap.append(a5)

        b6 = [time,bp6,bv6]
        a6 = [time,ap6,av6]
        sbp.append(b6)
        sap.append(a6)

        b7 = [time,bp7,bv7]
        a7 = [time,ap7,av7]
        sbp.append(b7)
        sap.append(a7)

        b8 = [time,bp8,bv8]
        a8 = [time,ap8,av8]
        sbp.append(b8)
        sap.append(a8)

        b9 = [time,bp9,bv9]
        a9 = [time,ap9,av9]
        sbp.append(b9)
        sap.append(a9)

        b10 = [time,bp10,bv10]
        a10 = [time,ap10,av10]
        sbp.append(b10)
        sap.append(a10)



# 将python object写入json文件
with open('data_ap_list.js',"w") as f:
    f.write("data1 = ")
    json.dump(sap, f)

with open('data_bp_list.js',"w") as f:
    f.write("data2 = ")
    json.dump(sbp, f)
    
# 直接打开html文件
url = 'C:\\Users\\shihan.ran\\Desktop\\xy-inv\\Visualization\\echarts_scatter.html'
webbrowser.open_new(url)







