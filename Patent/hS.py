# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 14:17
# @Author  : shihan.ran
# @Site    :
# @File    : test.py
# @Software: PyCharm

import xml.dom.minidom
import csv
import sys
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

    applicant = root.getElementsByTagName('business:Applicant')
    app_name = ''
    count = 0
    for each in applicant:
        count = count + 1
    if count > 1:
        i = 0
        for each in applicant:
            # address = each.getElementsByTagName('base:AddressBook')
            i = i + 1
            name = each.getElementsByTagName('base:Name')[0].firstChild.data
            if i == count:
                app_name = app_name + name
            else:
                app_name = app_name + name + ';'
    else:
        app_name = applicant[0].getElementsByTagName('base:Name')[0].firstChild.data

    post = root.getElementsByTagName('base:PostCode')[0].firstChild.data
    place = root.getElementsByTagName('business:ApplicantDetails')[0].getElementsByTagName('base:Text')[0].firstChild.data.replace(post, '').replace(' ', '')

    inventor = root.getElementsByTagName('business:Inventor')
    inv_name = ''
    count = 0
    for each in inventor:
        count = count + 1
    if count > 1:
        i = 0
        for each in inventor:
            # address = each.getElementsByTagName('base:AddressBook')
            i = i + 1
            name = each.getElementsByTagName('base:Name')[0].firstChild.data
            if i == count:
                inv_name = inv_name + name
            else:
                inv_name = inv_name + name + ';'
    else:
        inv_name = inventor[0].getElementsByTagName('base:Name')[0].firstChild.data
    # agency = root.getElementsByTagName('base:OrganizationName')[0].firstChild.datatest
    # detail = root.getElementsByTagName('base:Paragraphs')[0].firstChild.datatest

    print u'申请号：', shenqinghao
    print u'申请日：', shenqingri
    print u'公开号：', gongkaihao
    print u'公开日：', gongkairi
    print u'IPC分类号：', IPCfenleihao
    print u'申请人：', app_name
    print u'发明人：', inv_name
    print u'专利产品：',title
    # print u'代理人：', agency
    print u'申请人地址：', place
    print u'申请人邮编：', post

    return [shenqinghao, shenqingri, gongkaihao, gongkairi, IPCfenleihao, app_name, inv_name, title, place, post]


if __name__ == '__main__':

    try:
        result = get_each_invent('a.XML')
    except IOError:
        print('cant open')