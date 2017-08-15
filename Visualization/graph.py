import seaborn as sns
import numpy as np
import pandas as pd
import csv
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt

reader = csv.reader(open("data.csv"))
for contradiction,time,lastprice,volume,bp1,bv1,bp2,bv2,bp3,bv3,\
                                     bp4,bv4,bp5,bv5,bp6,bv6,bp7,bv7,bp8,bv8,bp9,bv9,bp10,bv10,\
                                     ap1, av1, ap2, av2, ap3, av3,ap4, av4, ap5, av5, ap6, av6,\
                                     ap7, av7, ap8, av8, ap9, av9,ap10, av10 in reader:

    tm = [time]
    bp = [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,bp9,bp10]
    ap = [ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8,ap9,ap10]
    print(bp)

    axes = plt.subplot(111)
    type1 = axes.scatter(ap, bp, s=20, c='red')
    type3 = axes.scatter(bp, ap, s=50, c='blue')

    plt.xlabel(u'time')
    plt.ylabel(u'price')
    plt.show()
