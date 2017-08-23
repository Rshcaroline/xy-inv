# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 9:54
# @Author  : shihan.ran
# @Site    : 
# @File    : Match_company.py
# @Software: PyCharm

import re
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def Levenshtein(first, second):  # 编辑距离算法 计算字符串的相似度
    if len(first) > len(second):
        first, second = second, first
    if len(first) == 0:
        return len(second)
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for x in range(first_length)]

    # print distance_matrix
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    # print distance_matrix
    return distance_matrix[first_length - 1][second_length - 1]


if __name__ == '__main__':
    readap = csv.reader(open('Applicant.csv', 'rb'))
    for shenqinghao, shenqingri, gongkaihao, gongkairi, IPCfenleihao, applicant, inventor, title, place, post in readap:
        count = 1
        threshold = len(applicant) * 0.5  # 设置一个比较的阈值
        readcp = csv.reader(open('Company.csv', 'rb'))
        for InnerCode, SecuCode, ChiName, ChiNameAbbr in readcp:
            possible = 0

            # 尝试Levenshtein直接匹配applicant and ChiName
            LevenshteinDistance = Levenshtein(applicant, ChiName)
            if LevenshteinDistance <= threshold:
                possible = 1

            # 尝试包含
            res = re.findall(ChiNameAbbr, applicant)  # 查询出所有的匹配字符串 ChiNameAbbr in applicant
            if res:
                # print "There are %d parts:\n" % len(res)
                # for r in res:
                    # print r
                print ChiNameAbbr, applicant
            '''
            else:
                print applicant, '和', ChiNameAbbr, '不匹配'
                continue
            '''

            if possible:
                print applicant, ChiName

        count += 1
        print count