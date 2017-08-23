# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 12:25
# @Author  : shihan.ran
# @Site    : 
# @File    : match.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2017/8/23 11:24
# @Author  : shihan.ran
# @Site    :
# @File    : test.py
# @Software: PyCharm

import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def Levenshtein(first, second):  # 编辑距离算法 计算字符串相似度
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


a = '百度'
b = '百度的'
threshold = len(a) * 0.5  # 设置一个阈值 * 0.22
if Levenshtein(a,b) <= threshold:
    print a , b
else:
    print '不匹配'

res = re.findall('百度','的百度科技的百度')
for r in res:
    print r