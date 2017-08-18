import numpy as np
import pandas as pd
import csv
import json
import webbrowser

reader = csv.reader(open("datatest.csv"))

sbp = []
sap = []

for contradiction, time, lastprice, volume, bp1, bv1, bp2, bv2, bp3, bv3, \
    bp4, bv4, bp5, bv5, bp6, bv6, bp7, bv7, bp8, bv8, bp9, bv9, bp10, bv10, \
    ap1, av1, ap2, av2, ap3, av3, ap4, av4, ap5, av5, ap6, av6, \
    ap7, av7, ap8, av8, ap9, av9, ap10, av10 in reader:

    if contradiction == 'ag1712':
        b1 = {'time':time,'bp':bp1,'bv':bv1}
        a1 = {'time':time,'ap':ap1,'av':av1}
        sbp.append(b1)
        sap.append(a1)

        b2 = {'time': time, 'bp': bp2, 'bv': bv2}
        a2 = {'time': time, 'ap': ap2, 'av': av2}
        sbp.append(b2)
        sap.append(a2)

        b3 = {'time': time, 'bp': bp3, 'bv': bv3}
        a3 = {'time': time, 'ap': ap3, 'av': av3}
        sbp.append(b3)
        sap.append(a3)

        b4 = {'time': time, 'bp': bp4, 'bv': bv4}
        a4 = {'time': time, 'ap': ap4, 'av': av4}
        sbp.append(b4)
        sap.append(a4)

        b5 = {'time': time, 'bp': bp5, 'bv': bv5}
        a5 = {'time': time, 'ap': ap5, 'av': av5}
        sbp.append(b5)
        sap.append(a5)

        b6 = {'time': time, 'bp': bp6, 'bv': bv6}
        a6 = {'time': time, 'ap': ap6, 'av': av6}
        sbp.append(b6)
        sap.append(a6)

        b7 = {'time': time, 'bp': bp7, 'bv': bv7}
        a7 = {'time': time, 'ap': ap7, 'av': av7}
        sbp.append(b7)
        sap.append(a7)

        b8 = {'time': time, 'bp': bp8, 'bv': bv8}
        a8 = {'time': time, 'ap': ap8, 'av': av8}
        sbp.append(b8)
        sap.append(a8)

        b9 = {'time': time, 'bp': bp9, 'bv': bv9}
        a9 = {'time': time, 'ap': ap9, 'av': av9}
        sbp.append(b9)
        sap.append(a9)

        b10 = {'time': time, 'bp': bp10, 'bv': bv10}
        a10 = {'time': time, 'ap': ap10, 'av': av10}
        sbp.append(b10)
        sap.append(a10)


# 将python object写入json文件
with open('data_ap_dict.json', "w") as f1:
    json.dump(sap,f1)

with open('data_bp_dict.json', "w") as f2:
    json.dump(sbp,f2)

