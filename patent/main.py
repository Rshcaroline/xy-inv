# -*- coding:utf-8 -*-

import xml.dom.minidom
import csv
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

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
    detail = root.getElementsByTagName('base:Paragraphs')[0].firstChild.data
    agency = root.getElementsByTagName('base:OrganizationName')[0].firstChild.data

    print u'申请号：', shenqinghao
    print u'申请日：', shenqingri
    print u'公开号：', gongkaihao
    print u'公开日：', gongkairi
    print u'IPC分类号：', IPCfenleihao
    print u'申请人：', name
    print u'发明人：', inventor
    print u'专利产品：',title
    print u'代理人：', agency
    print u'申请人地址：', place
    print u'申请人邮编：', post
    print u'介绍：',detail
    return [shenqinghao, shenqingri, gongkaihao, gongkairi, IPCfenleihao, name, inventor, title, agency, place, post, detail]


def write(r):
    outfile = open('test.csv', 'ab')
    writer = csv.writer(outfile)
    writer.writerow(r)
    outfile.close()
    return 0

if __name__ == '__main__':
    # result = get_each_invent('test.XML')
    # write(result)

    with open('index.txt') as f:
        cv = f.readlines()
        for line in cv:
            line = line.replace(u'\\', '/')
            print line
            time.sleep(3)
        f.close()
    print 'done'
