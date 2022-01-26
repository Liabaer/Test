# -*- coding: utf-8 -*-
# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
s1 = "this apple is sweet"
s2 = "this apple is sour"
s1_list = s1.split()
print s1_list

def to_list(s):
    """
    将字符串切割成数组 等同于s1_list = a.split()，s1_list = a.split(' ')空格是这样子
    :param s:传入字符串
    :return:返回数组
    """

    sa = []
    temp = ''
    i = 0
    while i < len(s):
        if s[i] != ' ':
            temp = temp + s[i]
            if i == len(s) - 1:
                sa.append(temp)
        if s[i] == ' ':
            sa.append(temp)
            temp = ''
            i = i + 1
            continue
        i = i + 1
    return sa


def to_dic(sa_new):
    """
    计算数组中每个单词出现的次数用字典存
    :param sa_new:要计算的数组
    :return:返回字典
    """
    s_dic = {}
    j = 0
    while j < len(sa_new):
        if sa_new[j] not in s_dic:
            s_dic[sa_new[j]] = 1
        else:
            s_dic[sa_new[j]] = s_dic[sa_new[j]] + 1

        j = j + 1
    return s_dic


def find_word(sd1, sd2):
    """
    计算出现在第一字典出现，第二个没出现，第二个出现，第一个没有出现的单词
    :param sd1: 字典1
    :param sd2: 字典2
    :return: 返回没出现的key单词
    """
    key = []
    for k, v in sd1.items():
        if v == 1 and k not in sd2:
            key.append(k)
    return key


sa_new = to_list(s1)
print sa_new
sdic = to_dic(sa_new)
print sdic

sa_new2 = to_list(s2)
print sa_new2
sdic2 = to_dic(sa_new2)
print sdic2

key1 = find_word(sdic, sdic2)
print key1
key2 = find_word(sdic2, sdic)
print key2
key_new = key1 + key2
print key_new
