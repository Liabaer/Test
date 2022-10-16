# -*- coding: utf-8 -*-
# 该题一共3个小问题，分别拆开成为3道题分别解答。1个文本文件作为本题目的输入数据，请按照源文件内 部说明修改代码，实现以下功能：
# 《命运》是著名科幻作家倪匡的作品。这里给出《命运》的一个网络本文件，文件名为“命运.txt”

# 问题一、(5分)在右侧修改代码，对“命运.txt"文件进行字符频次统计，
# 输出频次最高的中文字符（不包括 标点符号)及其频次，字符与频次之间采用英文冒号“："分隔，示例格式如下：

# 请在...处使用一行或多行代码替换

# f = open('命运.txt', encoding="utf-8")
# f_list = f.readlines()
# f_t = [':', ' ', '（', '）', '.', '/', '\n']
# d = {}
# for i in f_list:
#     for j in i:
#         if j not in f_t:
#             d[j] = d.get(j, 0) + 1
# # print(d)
# # d.tiems()就是将字典转化成元祖
# ds = list(d.items())
# # 对ds排序
# ds.sort(key=lambda x: x[1], reverse=True)
# # print(ds)
# print("{}:{}".format(ds[0][0],ds[0][1]))

# 问题二、(5分)在右侧的编程模板中修改代码，对"命运.xt"文件进行字符频次统计，
# 按照频次由高到低， 在屏幕输出前10个频次最高的字符，不包含回车符，字符之间无间隔，连续输出，示例格式如下；

# 请在...处使用一行或多行代码替换

# f = open('命运.txt', encoding="utf-8")
# f_list = f.readlines()
# f_t = [':', ' ', '（', '）', '.', '/', '\n']
# d = {}
# for i in f_list:
#     for j in i:
#         if j not in f_t:
#             d[j] = d.get(j, 0) + 1
# ls = list(d.items())
# ls.sort(key=lambda x: x[1], reverse=True) # 此行可以按照词频由高到低排序
# res = ls[0:10]
# for i in res:
#     print(i[0], end='')


# 问题三、(10分)在右侧修改代码，对“命运.xt"文件进行字符频次统计，
# 将所有字符按照频次从高到低排 序，字符包括中文、标点、英文等符号，但不包含空格和回车。将排序后的字符及频次输出到考生文件夹 下，文件名为“命运-频次排序txt”。字符与频次之间采用英文冒号"："分隔，各字符之间采用英文逗号”"分
# 隔，参考CSV格式，最后无逗号，文件内部示例格式如下：
#
f = open('../data/命运.txt', encoding="utf-8")
f_list = f.readlines()
f_t = [':', ' ', '（', '）', '.', '/', '\n']
d = {}
for i in f_list:
    for j in i:
        if j not in f_t:
            d[j] = d.get(j, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)  # 此行可以按照词频由高到低排序
count = 0
# 注意要加"a"，写入权限
f_new = open("../data/命运-频次排序.txt", "w", encoding="utf-8")
for i in ls:
    count = count + 1
    if count < len(ls):
        f_new.write(str(i[0]) + ':' + str(i[1]) + ',')
    else:
        f_new.write(str(i[0]) + ':' + str(i[1]))
