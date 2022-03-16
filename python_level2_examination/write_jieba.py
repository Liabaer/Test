# -*- coding: utf-8 -*-

#第一题
# 在考生文件夹下有个文件PY202.py,请编写代码替换省略号,完成如下功能。
# 止用户输入一首诗的文本,内部包含中文逗号和句号。
# (1)用eba库的精确模式对输入文本分词。将分词后的词语输出并以/"分隔;统计中文词语数并输出;
# (2)以逗号和句号将输入文本分隔成单句并 输出,每句一行,每行20个字符宽,居中对齐。"
# "在(1)和(2)的输出之间,增加一个空行 示例如下(其中数据仅用于示意):月亮河宽宽的河，一天我从你身旁过，

# import jieba
# jieba.setLogLevel(20)
# #
# # 以下代码....表示省略了一堆代码，大于等于一行代码
#
# s = input("请输入一段中文文本，句子之间以逗号或句号分割: ")
#
# slist = jieba.lcut(s)
#
# m = 0
# for i in slist:
#     if i in "，。":
#         continue
#     else:
#         m = m + 1
#         print(i, end='/')
# # slist = "/".join(slist)
# # print(slist)
# print("\n中文的词语数是: {}".format(m))
# j = 0
# res = '\n'
# while j < len(slist):
#     if slist[j] not in "，。":
#         res = res + slist[j]
#     else:
#         res = res + '\n'
#     j = j + 1
# print(res)

# 第二题
# 问题1:(10分)请编写程序，用Python语言中文分词第三方库jieba对文件datatxt进行分词，并将结果写入文件outtxt每行一个词，例如:
# 内容简介
# 编辑整个
# 故事
# 在
# 东汉
#
# ...

# 在右侧的程序框架文件中补充代码完成程序。
# import jieba
#
# f = open('data(4).txt', 'r')
# lines = f.readlines()
# f.close()
# f = open('out.txt','w')
# for line in lines:
#     line = line.strip()              #删除每行首尾可能出现的空格
#     wordList = jieba.lcut(line)         #用结巴分词，对每行内容进行分词
#     f.writelines('\n'.join(wordList))  #将分词结果存到文件out.txt中
# f.close()
# #
# 问题2：（10分)对文件out.txt进行分析，打印输出曹操出现的次数。
# 在右侧的代码框里补充代码完成程序，由于out.txt是你回答问题1生成的，应该继续 用该文件回答问题2。
# 系统为了让你掌握知识点，系统给出一个正确的out.txt,而 正式考试是不会给你的这个文件的， 需要用你自己的文件来解答下一问。

import jieba
f = open('out.txt', 'r')    #以读的方式打开文件
words = f.readlines()
f.close()
D={}
for w in words:        #词频统计
    D[w[:-1]]=D.get(w[:-1], 0) + 1
print("曹操出现次数为:{}  ".format(D['曹操']))