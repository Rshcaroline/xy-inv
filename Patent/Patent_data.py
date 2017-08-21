# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 9:37
# @Author  : shihan.ran
# @Site    : 
# @File    : Patent_data.py
# @Software: PyCharm

# zipfile
# Ftplib

import os
import ftplib

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
        print("LocalDir:", LocalDir)
        LocalNames = os.listdir(LocalDir)
        print("list:", LocalNames)
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
        print("remoteDir:", RemoteDir)
        if os.path.isdir(LocalDir) == False:
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        print("RemoteNames", RemoteNames)
        print(self.ftp.nlst("/del1"))  # nlst为获取目录下的文件
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if self.isDir(file):
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

    def DownLoadFileTree(self, LocalDir, RemoteDir):
        print("remoteDir:", RemoteDir)
        if os.path.isdir(LocalDir) == False:
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        print("RemoteNames", RemoteNames)
        # print(self.ftp.nlst("/del1"))  # nlst为获取目录下的文件
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            if self.isDir(file):
                self.DownLoadFileTree(Local, file)
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")
        return

if __name__ == "__main__":
    ftp = myFtp('patdata1ftp.sipo.gov.cn')
    ftp.Login(user='cbs_XYINV', passwd='N6148s')

    fls = []  # first ls
    itfls = []  # initial first ls 去掉前缀
    ftp.retrlines('LIST', callback=fls.append)  # 调用fls的append将每一个子目录存进fls中 ftp.retrlines功能与ftp.dir()类似
    for entry in fls:
        itfls.append(entry[55:])   # 因为前缀 len('drwxrwxrwx   1 user     group           0 Mar 17 14:45 ') = 55

    print(fls)
    print(itfls)

    ftp.cwd(itfls[5])  # 进入目录 'CN-BIBS-ABSS-10-A_中国发明专利申请公布标准化著录项目数据'

    sls = []  # second ls
    itsls = []  # initial second ls 去掉前缀
    ftp.retrlines('LIST', callback=sls.append)  # 调用sls的append将每一个子目录存进sls中
    for entry in sls:
        itsls.append(entry[55:])

    print(itsls)

    # ftp.DownLoadFileTree('C:\\Users\\shihan.ran\\Downloads', itsls[5])  # ok
    ftp.close()
    print("ok!")


