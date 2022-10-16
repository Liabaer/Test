# -*- coding: utf-8 -*-
# 在附件中有一个data.txt文件是一个来源于网上的技术信息资料。
# 问题1(10分)在右侧的编程框内，补充修改代码完成程序。用Python语言中文分 词第三方库jieba对文件data.txt进行分词，
# 并选择长度大于等于3个字符的关键词， 写入文件out1.txt,每行一个关键词，各行的关键词不重复，输出顺序不做要求，例 如：
# 人工智能
# 科幻小说
# import jieba
# # 解决jieba红标提示
# jieba.setLogLevel(20)
#
# f_vrp = open("vrp.txt")
# res = []
# f = open('out1(1).txt', 'w')
# temp = jieba.lcut(f_vrp.read())
# for i in temp:
#     if len(i) >= 3 and i not in res:
#         res.append(i)
# # 用join函数把res使用\n拼接起来  --->！！！res里面的元素一定要是字符串，否则不能使用join（join是拼接  split是分割）
# f.write('\n'.join(res))
# print(res)
# f.close()

#
# 问题2：（10分)右侧编程框中给出部分代码，补充完成程序，对文件data.txt进行 分词，
# 对长度不少于3个字符的关键词，统计出现的次数，按照出现次数由大到小的 顺序输出到文件out2.txt,每行一个关键词和出现次数，例如：
# 科学家：2
# 达特茅斯：1
import jieba

# 解决jieba红标提示
jieba.setLogLevel(20)
d = {}
f_vrp = open("../data/vrp.txt")
temp = jieba.lcut(f_vrp.read())
for i in temp:
    if len(i) >= 3:
        d[i] = d.get(i, 0) + 1
# print(d)
# 字典转换成元祖
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)  # 此行可以按照词频由高到低排序
print(ls)
with open("../data/out2.txt", 'w', encoding="utf-8") as fi:
    for i in ls:
        fi.write("{}:{}\n".format(i[0], str(i[1])))
