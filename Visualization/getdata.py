import numpy as np
import pandas as pd
import csv
import json
import webbrowser

def write(r):
    outfile = open('CN-BIBS-ABSS-10-B_20170718.csv', 'ab')
    writer = csv.writer(outfile)
    writer.writerow(r)
    outfile.close()
    return 0

reader = csv.reader(open("data.csv"))

sbp = []
sap = []

for contradiction, time, lastprice, volume, bp1, bv1, bp2, bv2, bp3, bv3, \
    bp4, bv4, bp5, bv5, bp6, bv6, bp7, bv7, bp8, bv8, bp9, bv9, bp10, bv10, \
    ap1, av1, ap2, av2, ap3, av3, ap4, av4, ap5, av5, ap6, av6, \
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

        b6 = [time, bp6, bv6]
        a6 = [time, ap6, av6]
        sbp.append(b6)
        sap.append(a6)

        b7 = [time, bp7, bv7]
        a7 = [time, ap7, av7]
        sbp.append(b7)
        sap.append(a7)

        b8 = [time, bp8, bv8]
        a8 = [time, ap8, av8]
        sbp.append(b8)
        sap.append(a8)

        b9 = [time, bp9, bv9]
        a9 = [time, ap9, av9]
        sbp.append(b9)
        sap.append(a9)

        b10 = [time, bp10, bv10]
        a10 = [time, ap10, av10]
        sbp.append(b10)
        sap.append(a10)

# 将python object写入json文件
with open('data_ap.json', "w") as f:
    for i in range(len(sap)):
        json.dump(sap[i], f)
        # json.dumps(sap[i],f)


# 直接打开html文件
url = 'C:\\Users\\shihan.ran\\Desktop\\xy-inv\\Visualization\\echarts_scatter.html'
webbrowser.open_new(url)




