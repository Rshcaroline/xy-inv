# xy-inv
an internship in XY investment company

## Patent

#### 环境：

Python 2.7

一定要注意环境，一开始我用3.6来写，因为3.6的编码默认成了unicode，尝试了很久总是在中文编码问题上报错。最后推翻全换成2.7，统一处理了编码问题才能正常运行。

```python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```

#### 主要思路为：

用公司申请的账号密码去专利网下载数据，按照专利文件夹的索引生成自己的索引去遍历文件，再处理XML文件。

> 我认为直接利用生成的索引去访问文件应该比直接用os库深度优先遍历文件夹的效率要高。

#### 成果：

主要利用ftplib和zipfile以及import xml.dom.minidom。
最后能做到从专利网的ftp自动下载数据，进行解压缩，再利用索引访问文件夹，处理XML文件，将扒好的数据存入csv文件中。

> 注：最后的csv文件是**utf-8**编码的，如果windows下直接打开csv，系统会用gbk编码来读入，所以会乱码。建议先处理文件或者使用编辑器打开。

#### 调用：

只需要更改main函数开头的两行代码：

update为更新日期，格式为"%y%m%d"，e.g.:20170822.

脚本会自动对比ftp目录下的日期，下载日期**大于等于**更新日期的。

```python
if update <= itsls[i+2]
```

dnpath为下载和解压的数据存放的绝对路径。脚本会自动创建文件夹存放文件，文件夹命名为"%y%m%d"。

```python
dnpath = 'C:\\Users\\shihan.ran\\Downloads'  # \\Downloads
```

对于第一层目录分类，可以通过更改itfls列表的索引值。比如itfls[5]为：CN-BIBS-ABSS-10-A中国发明专利申请公布标准化著录项目数据，对应的itfls[6]为CN-BIBS-ABSS-10-B中国发明专利授权公告标准化著录项目数据。

```python
enterls = itfls[5]
ftp.cwd(enterls)
```

#### 关于匹配数据：

Match_company是用于匹配申请人和上市公司的代码。利用了字符串子串来匹配上司公司简称和申请人，利用了编辑距离算法Levenshtein来对申请人和上市公司全称进行模糊匹配，精确度可以自己通过调整threshold来改变。

#### 写代码的时候主要需注意的是：

1. 注意路径的转义字符 要将'\\'变成'/'：
```python
line = line.replace(u'\\', '/')
```
2. 注意把每一行最后的隐含的\n去掉：
```python
line = line.replace(u'\n', '')
```



## Visualization

#### 环境：

Python 3.6

#### 主要思路为：

利用已有的数据写一个数据可视化界面出来，包含十个卖价十个买价以及成交量。

#### 成果：

从matplotlib到利用python+echarts作图。
最终的脚本getdatalist可以做到**把数据从txt读入 -> 处理去空格 -> 生成csv文件 -> 读入csv文件并生成js文件及全局变量。**
脚本的最后一行会直接自动打开浏览器，显示已经生成好的图片。
图片包含缩放轴，散点的半径的大小与成交量成正相关。

#### 调用：

原始数据的txt命名为：'in.txt'即可，并将其放入当前py文件目录下，运行getdatalist.py即可。

> 数据量不要太大，可能会把Pycharm搞崩，再者 做出来的图可能也不好看。

#### 写代码的时候主要需要注意的：
echarts的js文件的导入/json数据格式及与python的互换/html和js的语法/html调用json数据。示意图：



## Learning

主要是一些自己写着玩/下载的代码，包括一个wiki(利用dokuwiki)/贪吃蛇游戏(结合pygame)/与你最相似的人的推荐算法，以及一些自己看书的时候学的python语法。



## Btc

包含一些比特币交易所的api。
