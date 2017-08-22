# xy-inv
an internship in XY investment company


## Patent 
#### 环境：
Python 2.7
#### 主要思路为：
用公司申请的账号密码去专利网下载数据，按照专利文件夹的索引生成自己的索引，再处理XML文件。
#### 成果：
利用ftplib和zipfile以及import xml.dom.minidom。
从专利网的ftp自动下载数据，进行解压缩，再利用索引访问文件夹，处理XML文件，将扒好的数据存入csv文件中。
#### 调用：
只需要更改main函数开头的两行：
update为更新日期，格式为"%y%m%d"，e.g.:20170822.脚本会自动对比ftp目录下的日期，下载日期大于等于更新日期的。
```
if update <= itsls[i+2]
```
dnpath为下载和解压的数据存放的绝对路径。脚本会自动创建文件夹来存放文件。
```
dnpath = 'C:\\Users\\shihan.ran\\Downloads'  # \\Downloads
```
#### 主要需注意的是：</u>
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
从matplotlib到利用python+echarts作图
最终的脚本getdatalist可以做到把数据从txt读入/处理去空格/生成csv文件/读入csv文件并生成js文件及全局变量
脚本的最后一行可以直接自动打开浏览器，显示已经生成好的图片。
图片包含缩放轴，散点的半径与成交量成正相关。
#### 调用：
原始数据的txt命名为：'in.txt'即可，并将其放入当前py文件目录下即可。
#### 主要需要注意的：
echarts的js文件的导入/json数据格式及与python的互换/html和js的语法/html调用json数据。
数据量不要太大，可能会把Pycharm搞崩，再者 做出来的图可能也不好看。

## Learning
主要是一些自己写着玩/下载的代码，包括一个wiki(利用dokuwiki)/贪吃蛇游戏(结合pygame)/与你最相似的人的推荐算法，以及一些自己看书的时候学的python语法。

## btc
包含一些比特币交易所的api。
