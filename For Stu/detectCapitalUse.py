# -*- coding: utf-8 -*-
# 给定一个单词，你需要判断单词的大写使用是否正确。
# 我们定义，在以下情况时，单词的大写用法是正确的：
#
# 全部字母都是大写，比如"USA"。
# 单词中所有字母都不是大写，比如"leetcode"。
# 如果单词不只含有一个字母，只有首字母大写，比如"Google"。
# 否则，我们定义这个单词没有正确使用大写字母。
word = "Leetcode"

def is_uppercase(word_str):
    if 60 <= ord(word_str) <= 90:
        return True
    return False

def is_lowercase(word_str):
    if 97 <= ord(word_str) <= 122:
        return True
    return False

i = 0
flag = True

# print ord('a')
while i < len(word):
    if len(word) == 1:
        flag = True
        break
    if is_uppercase(word[0]):
        # 已经判断过第一个，所以不对第一位字母进行比较
        if i==0:
            i = i + 1
            continue
        if is_uppercase(word[i]) and is_uppercase(word[1]):
            flag = True
        elif is_lowercase(word[i]) and is_lowercase(word[1]):
            flag = True
        elif is_uppercase(word[i]) and is_lowercase(word[1]):
            print word[i]
            flag = False
            break
        elif is_lowercase(word[i]) and is_uppercase(word[1]):
            flag = False
            break
    else:
        if is_uppercase(word[i]):
            flag = False
            break
    i = i + 1
print flag
