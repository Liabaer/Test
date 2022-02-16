# -*- coding: utf-8 -*-
# 在考生文件夹下有个文件PY202.py,请编写代码替换省略号,完成如下功能。
# 止用户输入一首诗的文本,内部包含中文逗号和句号。
# (1)用eba库的精确模式对输入文本分词。将分词后的词语输出并以/"分隔;统计中文词语数并输出;
# (2)以逗号和句号将输入文本分隔成单句并 输出,每句一行,每行20个字符宽,居中对齐。"
# "在(1)和(2)的输出之间,增加一个空行 示例如下(其中数据仅用于示意):月亮河宽宽的河，一天我从你身旁过，

import jieba
jieba.setLogLevel(20)

# 以下代码....表示省略了一堆代码，大于等于一行代码

s = input("请输入一段中文文本，句子之间以逗号或句号分割: ")

slist = jieba.lcut(s)

m = 0
for i in slist:
    if i in "，。":
        continue
    else:
        m = m + 1
        print(i, end='/')
# slist = "/".join(slist)
# print(slist)
print("\n中文的词语数是: {}".format(m))
j = 0
res = '\n'
while j < len(slist):
    if slist[j] not in "，。":
        res = res + slist[j]
    else:
        res = res + '\n'
    j = j + 1
print(res)
