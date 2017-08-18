# xy-inv
an internship in XY investment company


## Patent 
#### 主要思路为：
用公司申请的账号密码去专利网下载数据，按照专利文件夹的索引index.txt读入每一行存入一个list中，格式如下：
```
\1\CN102015000436362CN00001065046750ABIAZH20170315CN00C\CN102015000436362CN00001065046750ABIAZH20170315CN00C.XML
```
#### 此时需注意的是：</u>
1. 注意在访问的时候应该是没有1前面那个\的，即：
```
1/CN102015000436362CN00001065046750ABIAZH20170315CN00C/CN102015000436362CN00001065046750ABIAZH20170315CN00C.XML
```
```python
line = line.replace(u'\\1\\', '1\\')
```
2. 注意路径的转义字符 要将'\\'变成'/'：
```python
line = line.replace(u'\\', '/')
```
3. 注意把每一行最后的隐含的\n去掉：
```python
line = line.replace(u'\n', '')
```
#### 处理XML文件：
利用一个叫xml.dom.minidom的包即可，再输出到csv文件。

## Visualization
#### 主要思路为：
利用已有的数据写一个数据可视化界面出来，包含十个卖价十个买价以及成交量。
#### 成果：
从matplotlib到利用python+echarts作图
最终的脚本getdatalist可以做到把数据从txt读入/处理去空格/生成csv文件/读入csv文件并生成js文件及全局变量
脚本的最后一行可以直接自动打开浏览器，显示已经生成好的图片。
图片包含缩放轴，散点的半径与成交量成正相关。
#### 主要需要注意的：
echarts的js文件的导入/json数据格式及与python的互换/html和js的语法/html调用json数据。

## Learning
主要是一些自己写着玩/下载的代码，包括一个wiki(利用dokuwiki)/贪吃蛇游戏(结合pygame)/与你最相似的人的推荐算法，以及一些自己看书的时候学的python语法。

## btc
包含一些比特币交易所的api。
