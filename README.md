# xy-inv
an internship in XY investment company


## Patent 
### 主要思路为：<br>
用公司申请的账号密码去专利网下载数据，按照专利文件夹的索引index.txt读入每一行存入一个list中，格式如下：<br>
```
\1\CN102015000436362CN00001065046750ABIAZH20170315CN00C\CN102015000436362CN00001065046750ABIAZH20170315CN00C.XML
```
#### 此时需`注意`的是：<br>
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
### 处理XML文件：
利用一个叫xml.dom.minidom的包即可，再输出到csv文件。
