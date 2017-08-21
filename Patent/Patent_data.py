# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 9:37
# @Author  : shihan.ran
# @Site    : 
# @File    : Patent_data.py
# @Software: PyCharm

# zipfile
# Ftplib

import os
import time
import ftplib
import zipfile
import csv
import xml.dom.minidom

class myFtp:
    ftp = ftplib.FTP()
    bIsDir = False
    path = ""

    def __init__(self, host):
        # self.ftp.set_debuglevel(2) # 打开调试级别2，显示详细信息
        # self.ftp.set_pasv(0)      # 0主动模式 1被动模式
        self.ftp.connect(host)
        self.ftp.encoding = 'GB18030'  # 切换编码格式 不然中文会出现乱码

    def Login(self, user, passwd):
        self.ftp.login(user, passwd)
        print(self.ftp.welcome)

    def DownLoadFile(self, LocalFile, RemoteFile):
        print('正在下载的文件为：',RemoteFile)
        file_handler = open(LocalFile, 'wb')
        self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write)
        file_handler.close()
        return True

    def UpLoadFile(self, LocalFile, RemoteFile):
        if os.path.isfile(LocalFile) == False:
            return False
        file_handler = open(LocalFile, "rb")
        self.ftp.storbinary('STOR %s' % RemoteFile, file_handler, 4096)
        file_handler.close()
        return True

    def UpLoadFileTree(self, LocalDir, RemoteDir):
        if os.path.isdir(LocalDir) == False:
            return False
        print("本地上传地址为：", LocalDir)
        LocalNames = os.listdir(LocalDir)
        print("上传文件名为:", LocalNames)
        print(RemoteDir)
        self.ftp.cwd(RemoteDir)
        for Local in LocalNames:
            src = os.path.join(LocalDir, Local)
            if os.path.isdir(src):
                self.UpLoadFileTree(src, Local)
            else:
                self.UpLoadFile(src, Local)
        self.ftp.cwd("..")
        return

    def DownLoadFileTree(self, LocalDir, RemoteDir):
        print("正在下载的目录为:", RemoteDir)
        if os.path.isdir(LocalDir) == False:  # 如果本地没有目录
            os.makedirs(LocalDir)  # 新建一个目录保存下载文件
        self.ftp.cwd(RemoteDir)   # 进入下载目录
        RemoteNames = self.ftp.nlst()  # 将目录下的所有文件名存入
        print("需要下载的文件为：", RemoteNames)
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)   # 将本地路径和文件名合成一个绝对路径
            if self.isDir(file):     # 如果仍为一个目录 则用深度优先遍历
                self.DownLoadFileTree(Local, file)
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")
        return

    def show(self, list):
        result = list.lower().split(" ")
        if self.path in result and "<dir>" in result:
            self.bIsDir = True

    def isDir(self, path):
        self.bIsDir = False
        self.path = path
        # this ues callback function ,that will change bIsDir value
        self.ftp.retrlines('LIST', self.show)
        return self.bIsDir

    def retrlines(self, path, callback):
        self.ftp.retrlines(path, callback=callback)

    def encoding(self, encoding):
        self.ftp.encoding = encoding

    def cwd(self,path):
        self.ftp.cwd(path)

    def close(self):
        self.ftp.quit()

def get_each_invent(f):
    dom = xml.dom.minidom.parse(f)
    root = dom.documentElement

    gongkai = root.getElementsByTagName('business:PublicationReference')[1]
    gongkaihao = gongkai.getElementsByTagName('base:WIPOST3Code')[0].firstChild.data + gongkai.getElementsByTagName('base:DocNumber')[0].firstChild.data + gongkai.getElementsByTagName('base:Kind')[0].firstChild.data
    gongkairi = gongkai.getElementsByTagName('base:Date')[0].firstChild.data
    shenqing = root.getElementsByTagName('business:ApplicationReference')[1]
    shenqinghao = shenqing.getElementsByTagName('base:WIPOST3Code')[0].firstChild.data + shenqing.getElementsByTagName('base:DocNumber')[0].firstChild.data
    shenqingri = shenqing.getElementsByTagName('base:Date')[0].firstChild.data
    IPCfenlei = root.getElementsByTagName('business:ClassificationIPCR')
    IPCfenleihao = ''
    for each in IPCfenlei:
        IPCfenleihao = IPCfenleihao + each.getElementsByTagName('business:Section')[0].firstChild.data + each.getElementsByTagName('business:MainClass')[0].firstChild.data + each.getElementsByTagName('business:Subclass')[0].firstChild.data + each.getElementsByTagName('business:MainGroup')[0].firstChild.data + '/' + each.getElementsByTagName('business:Subgroup')[0].firstChild.data + ';'
    title = root.getElementsByTagName('business:InventionTitle')[0].firstChild.data
    name = root.getElementsByTagName('base:Name')[0].firstChild.data
    post = root.getElementsByTagName('base:PostCode')[0].firstChild.data
    place = root.getElementsByTagName('business:ApplicantDetails')[0].getElementsByTagName('base:Text')[0].firstChild.data.replace(post, '').replace(' ', '')
    inventor = root.getElementsByTagName('base:Name')[1].firstChild.data
    # agency = root.getElementsByTagName('base:OrganizationName')[0].firstChild.datatest
    # detail = root.getElementsByTagName('base:Paragraphs')[0].firstChild.datatest

    print(u'申请号：', shenqinghao)
    print(u'申请日：', shenqingri)
    print(u'公开号：', gongkaihao)
    print(u'公开日：', gongkairi)
    print(u'IPC分类号：', IPCfenleihao)
    print(u'申请人：', name)
    print(u'发明人：', inventor)
    print(u'专利产品：',title)
    # print u'代理人：', agency
    print(u'申请人地址：', place)
    print(u'申请人邮编：', post)
    return [shenqinghao, shenqingri, gongkaihao, gongkairi, IPCfenleihao, name, inventor, title, place, post]

if __name__ == "__main__":
    update = '20170814'
    dnpath = 'C:\\Users\\shihan.ran\\Downloads'  # \\Downloads

    ftp = myFtp('patdata1ftp.sipo.gov.cn')
    ftp.Login(user='cbs_XYINV', passwd='N6148s')

    fls = []  # first ls
    itfls = []  # initial first ls 去掉前缀
    ftp.retrlines('LIST', callback=fls.append)  # 调用fls的append将每一个子目录存进fls中 ftp.retrlines功能与ftp.dir()类似
    for entry in fls:
        itfls.append(entry[55:])   # 因为前缀 len('drwxrwxrwx   1 user     group           0 Mar 17 14:45 ') = 55

    print('第一层目录下：',itfls)

    enterls = itfls[5]
    ftp.cwd(enterls)  # 进入目录 'CN-BIBS-ABSS-10-A_中国发明专利申请公布标准化著录项目数据'

    sls = []  # second ls
    itsls = []  # initial second ls 去掉前缀
    ftp.retrlines('LIST', callback=sls.append)  # 调用sls的append将每一个子目录存进sls中
    for entry in sls:
        itsls.append(entry[55:])

    print('第二层目录下：',itsls)

    download = []
    for i in range(len(itsls)-2):
        if update <= itsls[i+2]:
            download.append(itsls[i+2])

    print('需要更新的文件为：', download)

    st = time.clock()
    for file in download:
        # ftp.DownLoadFileTree(dnpath, file)  # file 现在是日期

        wt = enterls[0:13] + file + '.csv'  # 输出文件名
        print(wt)
        rd = dnpath + '\\' + file + '-INDEX-001.txt' # 读入的txt索引
        rd = rd.replace(u'\\', '/')  # 去掉\\对于路径的干扰
        print(rd)

        with open(rd) as infile, open(wt, 'ab') as outfile:
            cv = infile.readlines()
            writer = csv.writer(outfile)

            for line in cv:
                line = dnpath + '\\' + file + '-' + line[1] + '-001.ZIP' + line
                print(line)

                line = line.replace(u'\\', '/')
                line = line.replace(u'\n', '')
                print(line)

                try:
                    result = get_each_invent(line)
                    writer.writerow(result)
                except IOError:
                    print('cant open')

            infile.close()
            outfile.close()
    ftp.close()

    print("Done!")
    print('请更新脚本中的update为：', time.strftime('%Y%m%d',time.localtime(time.time())))




