import seaborn as sns
import numpy as np
import pandas as pd
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt

reader = csv.reader(open("data.csv"))

stm = []
sbp = []
sap = []

for contradiction, time, lastprice, volume, bp1, bv1, bp2, bv2, bp3, bv3, \
    bp4, bv4, bp5, bv5, bp6, bv6, bp7, bv7, bp8, bv8, bp9, bv9, bp10, bv10, \
    ap1, av1, ap2, av2, ap3, av3, ap4, av4, ap5, av5, ap6, av6, \
    ap7, av7, ap8, av8, ap9, av9, ap10, av10 in reader:

    if contradiction == 'ag1707':
        tm = [time, time, time, time, time, time, time, time, time, time]
        bp = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, bp9, bp10]
        ap = [ap1, ap2, ap3, ap4, ap5, ap6, ap7, ap8, ap9, ap10]

        bp = [np.NaN if x == 0 else x for x in bp]
        ap = [np.NaN if x == 0 else x for x in ap]

        stm.append(tm)
        sbp.append(bp)
        sap.append(ap)

        # print(len(stm), len(sbp), len(sap))
        # print(stm, sbp, sap)

        '''
        axes = plt.subplot(111)
        type1 = axes.scatter(tm, bp, s=20, c='red')
        type3 = axes.scatter(tm, ap, s=50, c='blue')
    
        plt.xlabel('time')
        plt.ylabel('price')
        plt.show()
        '''

        plt.title("I'm a scatter diagram.")
        # plt.xlim(xmax= 2190, xmin=time)
        # plt.ylim(ymax=bp1, ymin=bp10)
        plt.xlabel("time")
        plt.ylabel("price")
        axes = plt.subplot(111)

        for i in range(len(stm)):
            print(np.shape(stm[i]), np.shape(sbp[i]), np.shape(sap[i]))
            print(stm[i], sbp[i], sap[i])
            typebp = axes.scatter(stm[i], sbp[i], s=20, c='blue')
            typeap = axes.scatter(stm[i], sap[i], s=50, c='red')
            # plt.plot(tm, bp, 'ro', c='blue')
            # plt.plot(tm, ap, 'ro', c='red')
        plt.show()
    else:
        continue