# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 9:37
# @Author  : shihan.ran
# @Site    : 
# @File    : Patent_data.py
# @Software: PyCharm

# zipfile
# Ftplib

from ftplib import FTP

ftp = FTP(host='patdata1ftp.sipo.gov.cn')     # connect to host, default port

ftp.login(user='cbs_XYINV',passwd='N6148s')                     # user anonymous, passwd anonymous@

print(ftp.getwelcome())            # 打印出欢迎信息

ftp.encoding = 'GB18030'          # 切换编码格式 不然中文会出现乱码

fls = []  # first ls
itfls = []  # initial first ls 去掉前缀
ftp.retrlines('LIST', callback= fls.append)  # 调用fls的append将每一个子目录存进fls中 ftp.retrlines功能与ftp.dir()类似
for entry in fls:
    itfls.append(entry[55:])  # 因为 len('drwxrwxrwx   1 user     group           0 Mar 17 14:45 ') = 55

ftp.cwd(itfls[5])    # 进入目录 'CN-BIBS-ABSS-10-A_中国发明专利申请公布标准化著录项目数据'

sls = []  # second ls
itsls = []  # initial second ls 去掉前缀
ftp.retrlines('LIST', callback= sls.append)  # 调用sls的append将每一个子目录存进sls中
for entry in sls:
    itsls.append(entry[55:])

print(itsls)