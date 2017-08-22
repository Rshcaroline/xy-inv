# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 9:38
# @Author  : shihan.ran
# @Site    : 
# @File    : ziptest.py
# @Software: PyCharm

import zipfile

zippath = 'C:\\Users\\shihan.ran\\Downloads\\20170815-1-001.ZIP'
zippath = zippath.replace(u'\\', '/')

topath = 'C:\\Users\\shihan.ran\\Downloads\\20170815-1-001'
topath = topath.replace(u'\\', '/')

with zipfile.ZipFile(zippath) as myzip:
        myzip.extractall(topath)