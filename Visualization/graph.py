import seaborn as sns
import numpy as np
from numpy.random import randn
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats


# style set 这里只是一些简单的style设置
sns.set_palette('deep', desat=.6)
sns.set_context(rc={'figure.figsize': (8, 5) } )
np.random.seed(1425)  # 固定随机数种子 让每次产生的随机数是一样的
# figsize 是常用的参数.


'''
# 一个简单的直方图
data = randn(75)
plt.hist(data, bins=12, color=sns.desaturate("indianred", .8), alpha=.4)  # 用参数改变颜色
print(data)
plt.show()  # 加了这句话才会弹出图像框
'''


'''
# 以上数据是单总体 以下是双总体的hist
data1 = stats.poisson(2).rvs(100)
data2 = stats.poisson(5).rvs(500)

max_data = np.r_[data1, data2].max()
bins = np.linspace(0, max_data, max_data+1)

# 首先将2个图形分别画到figure中 弹出来两个单独的框
plt.hist(data1, bins, normed=True, color="#FF0000", alpha=.9)
plt.figure()
plt.hist(data2, bins, normed=True, color="#C1F320", alpha=.5)
plt.show()

# 观察下面图形 可以看出normed参数的作用 --
# 首先还是各自绘出自己的分布hist, 然后将二者重合部分用第三颜色加以区别.
plt.hist(data1, bins, normed=True, color="#FF0000", alpha=.9)
plt.hist(data2, bins, normed=True, color="#C1F320", alpha=.5)
plt.show()
'''


