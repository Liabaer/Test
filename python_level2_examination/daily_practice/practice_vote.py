# -*- coding: utf-8 -*-
# 使用字典和列表型变量完成最有人气的明星的投票数据分析。投票信息由附件里的 文件vote.txt给出，一行只有一个明星姓名的投票才是有效票。
# 有效票中得票最多 的明星当选最有人气的明星。
# 问题一：请统计有效票张数。在编程模板中补充代码完成程序。

# f = open("vote.txt", encoding="utf-8")
# names = f.readlines()
# f.close()
# n = 0
# for name in names:
#     num = len(name.split(' '))
#     if num == 1:
#         n += 1
# print("有效票{}张".format(n))

# 问题二：请给出当选最有人气明星的姓名和票数，右侧编程模板中补全代码，可删除 横线，随意修改代码，完成程序。
# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("../data/vote.txt", encoding="utf-8")
names = f.readlines()
f.close()
D = {}
for name in names:
    if len(name.split(' ')) == 1:
        D[name[:-1]] = D.get(name[:-1], 0) + 1
l = list(D.items())
l.sort(key=lambda s: s[1], reverse=True)
name = l[0][0]
score = l[0][1]
print("最具人气明星为:{},票数为:{}".format(name, score))
