# -*- coding: utf-8 -*-
# 使用字典和列表型变量完成村长选举。某村有40名有选举权和被选举权的村民，名 单在附件name.txt中，
# 从这40名村民中选出一人当村长，40人的投票信息由附件 vote.txt中给出，每行是一张选票的信息，有效票中得票最多的村民当选。
# 问题：请从vote.txt中筛选出无效票写入文件vote1.txt。有效票的含义是：选票中只 有一个名字且该名字在name.txt文件列表中，不是有效票的票称之为无效票。
f = open("../data/name.txt")
names = f.readlines()
# print(names)
f.close()
f = open("../data/vote.txt")
votes = f.readlines()
# print(votes)
f.close()
D = {}
NUM = 0
for vote in votes:
    num = len(vote.split())
    # print(vote)
    if num == 1 and vote in names:
        # D[vote[:-1]] = D[(vote[:-1]] + 1 这样会报错，因为没有处理vote[:-1没有出现在字典里的情况
        # vote[:-1] 是去掉回车符       d.get(x)/d.get(x, 0)可以获取字典的值 这里在d里面就+1，第一次出现的就是D[vote[:-1]] = 0 + 1
        D[vote[:-1]] = D.get(vote[:-1], 0) + 1
        NUM += 1
    else:
        with open("../data/vote1.txt", "a+", encoding="utf-8") as fi:
            fi.write("{}".format(vote))
print(D)

d = {'a': 1, "b": 2}
value = 10
# get函数获取字典key对应的value, 如果不存在key,则返回value
print(d.get('c', value))
