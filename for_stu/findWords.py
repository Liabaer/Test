# -*- coding: utf-8 -*-
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#
# 美式键盘 中：
#
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
one = "qwertyuiop"
two = "asdfghjkl"
three = "zxcvbnm"

words = ["omk"]
res = []
i = 0

while i < len(words):
    j = 0
    flagA = True
    flagB = True
    flagC = True
    temp = ''
    while j < len(words[i]):
        # 将字符串转换成小写
        if 65 <= ord(words[i][j]) <= 90:
            # print(chr(ord(s[i]) + 32))
            # chr()将asscii码转换成字母，ord(）求字母的asscii码
            temp = str(chr(ord(words[i][j]) + 32))
        else:
            temp = words[i][j]
        print(temp)
        if temp not in one:
            flagA = False

        if temp not in two:
            flagB = False

        if temp not in three:
            flagC = False
        j = j + 1
    if flagA or flagB or flagC:
        res.append(words[i])
    i = i + 1
print(res)