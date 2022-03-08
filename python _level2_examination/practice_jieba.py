# -*- coding: utf-8 -*-
# 在附件中有一个data.txt文件是一个来源于网上的技术信息资料。
# 问题1(10分)在右侧的编程框内，补充修改代码完成程序。用Python语言中文分 词第三方库jieba对文件data.txt进行分词，
# 并选择长度大于等于3个字符的关键词， 写入文件out1.txt,每行一个关键词，各行的关键词不重复，输出顺序不做要求，例 如：
# 人工智能
# 科幻小说
import jieba
# 解决jieba红标提示
jieba.setLogLevel(20)

f_vrp = open("vrp.txt")
res = []
f = open('out1(1).txt', 'w')
temp = jieba.lcut(f_vrp.read())
for i in temp:
    if len(i) >= 3 and i not in res:
        res.append(i)
# 用join函数把res使用\n拼接起来  --->！！！res里面的元素一定要是字符串，否则不能使用join（join是拼接  split是分割）
f.write('\n'.join(res))
print(res)
f.close()