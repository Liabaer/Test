# -*- coding: utf-8 -*-
# 给出第一个词first和第二个词second,考虑在某些文本text中可能以"first second third"形式出现的情况，其 中second紧随first出现，third紧随second出现。
# 对于每种这样的情况，将第三个词"third"添加到答案中，并返回答案。
text = "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
first = "lnlqhmaohv"
second = "ypkk"
new_text = []
i = 0
temp = ''
while i < len(text):
    if text[i] == ' ':
        new_text.append(temp)
        temp = ''
    else:
        temp += text[i]
    i = i + 1
if temp != '':
    new_text.append(temp)
print(new_text)

i = 0
flag = False
res = []
while i < len(new_text):
    if i+1 < len(new_text):
        if new_text[i] == first and new_text[i+1] == second:
            flag = True
        else:
            flag = False
    if flag and i+2 < len(new_text):
        res.append(new_text[i+2])
    i = i + 1
print(res)
