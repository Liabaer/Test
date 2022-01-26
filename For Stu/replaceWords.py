# -*- coding: utf-8 -*-
# 在英语中，我们有一个叫做词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为继承词(successor)。
# 例如，词根an，跟随着单词other(其他)，可以形成新的单词another(另一个)。
# 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。
# 你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
# 你需要输出替换之后的句子。
dictionary = ["cat", "bat", "rat"]
dictionary = set(dictionary)
print(dictionary)
sentence = "the cattle was rattled by the battery"
i = 0
s = ''
temp = []
while i < len(sentence):
    if sentence[i] != ' ':
        s = s + sentence[i]
    else:
        temp.append(s)
        s = ''
        i = i + 1
        continue
    i = i + 1
# s 最后一次没有遇到空格，直接append进数组
if s != '':
    temp.append(s)
print(temp)
m = 0
ans = []
while m < len(temp):
    n = 0
    l = ''
    flag = False
    while n < len(temp[m]):
        l = l + temp[m][n]
        if l in dictionary:
            ans.append(l)
            flag = True
            break
        else:
            n = n + 1
            continue
        print(l)
        n = n + 1
    if not flag:
        ans.append(l)
    m = m + 1
print(ans)
res = ''
res = ' '.join(ans)
# for j in range(0, len(ans)):
#     if j == 0:
#         res = res + ans[j]
#     else:
#         res = res + ' ' + ans[j]
print(res)
