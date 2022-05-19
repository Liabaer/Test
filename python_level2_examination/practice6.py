# -*- coding: utf-8 -*-
# 1
# 调用随机数库生成包含10个1-100之间的整数随机数的列表，然后删除列表中的偶 数，用逗号隔开，输出生成和删除后的数据，显示在屏幕上
# import random as r
#
# r.seed(1)
# nl = []
# for i in range(10):
#     nl.append(r.randint(1, 100))
# print(nl)
# newl = []
# for n in nl:
#     if n % 2 != 0:
#         newl.append(n)
# print(','.join(str(i) for i in newl))

# # 2
# 输入一个密码字符串，依次检查下述的条件：
# ·大于8个字符
# ·必须有一个字母或者一个数字
# 如果小于8个字符，就显示“密码长度要大于8个字符，请重新输入”
# 如果全是字母，就显示“密码要包含数字，请重新输入”
# 如果全是数字，就显示“密码要包含字母，请重新输入”
# 如果大于等于8个字符，并且既包含字母也包含数字，就显示“你的密码合格了”

# 在_____处填写一行代码
# 不允许修改其他代码
# while True:
#     s = input()
#     if len(s) < 8:
#         print('密码长度要大于8个字符，请重新输入')
#     #     反向判断，判断s.isdigit()是否纯数字
#     elif s.isdigit():
#         print('密码要包含字母，请重新输入')
#     #     反向判断，判断s.isalpha()是否纯字母
#     elif s.isalpha():
#         print('密码要包含数字，请重新输入')
#     else:
#         print('你的密码合格了')
#         break

# 3
# 从键盘输入一个多位数字的整数，按照从最高位到个位数的顺序，拆解成单个数字，显示在屏幕上。
# x = input()
# flag = True
# t = pow(10, len(x) - 1)
# x = eval(x)
# while True:
#     # divmod 取模  返回x // t 和 x % t的结果  是一个元祖
#     y, x = divmod(x, t)
#     print('{}'.format(y), end=' ')
#     t = t//10
#     if t == 0:
#         break

# 4
# 请输出所有满足以下条件的3位整数：该数是素数，该数的个位数字与十位数字之和 被10除所得余数恰好是该数的百位数字。
# 例如211是素数，并且（1+1)被10除的余数 是2，因此211是满足条件的3位素数。
#
# for i in range(100, 1000):
#     flag = True
#     x = i // 100
#     y = i // 10 % 10   # 234，i // 10 会去掉个位，变成23，然后对10取余数就可以得到3了
#     z = i - x * 100 - y * 10
#     for j in range(2, i):
#         if i % j != 0 and i != j:
#             flag = true是素数
#             flag = True
#         else:
#             flag = False
#             break
#     全部循环完，利用 flag 来判断是否满足条件
#     if flag:
#         if (z+y) % 10 == x:
#             print(i)

# 5
# 编写Python程序计算下列数学表达式的结果并输出，小数点后保留3位。
#
# x = (pow(3,4) + 5*(pow(6, 7)))/8
# print("{:.3f}".format(pow(x, 1/2)))

# 6
# 输入三个英文单词，用逗号隔开，按字典顺序输出显示在屏幕上。使用分号间隔 输入c,a,b输出a;b;c
# x = input()
# a = sorted(x.replace(',', ''))
# print(';'.join(a))

# 7
# 获得用户输入的一个数字，替换其中0-9为中文字符“○一二三四五六七
# 八九”，输出替换后结果。例如输入0，输出为○（中文字符)，参考编 程模板，完善代码。
# n = input("")
# s = "〇一二三四五六七八九"
# for c in "0123456789":
#     n = n.replace(c, s[eval(c)])
# print(n)

# # 8
# 文件figures.txt中包含了turtle画图所需要的数据，请读取数据，并根据数据中的参 数，
# 调用turtle库函数，画出数据所描述的多边螺旋线图形来，每一行代表一个图 形。
# 参数的格式定义为：图形的起始点xO,y0;图形的层数，图形的边数，图形的 颜色；
# 0,0,3,5,'red'
# 80,80,5,6,'blue
# -80,-80,4,4,'purple
# 50,0,8,10,'orange
# -50,60,5,7,'green
# import turtle as t
#
#
# def oneFigure(x0, y0, layer, edgenum, color):
#     """
#     todo 注释
#     :param x0:坐标x
#     :param y0:坐标y
#     :param layer:图形层数
#     :param edgenum:边数
#     :param color:颜色
#     :return:返回这个图形
#     """
#     d = 0
#     k = 1
#     t.penup()
#     t.goto(x0, y0)
#     t.pendown()
#     t.pencolor(color)
#     for j in range(layer):
#         for i in range(edgenum):
#             t.fd(k)
#             d = d + 360 // edgenum
#             t.seth(d)
#             k += 1
#
#
# with open("figures.txt", 'r') as f:
#     for l in f.readlines():
#         l = l.strip()
#         temp = l.split(',')
#         print(temp)
#         x = int(temp[0])
#         y = int(temp[1])
#         la = int(temp[2])
#         ed = int(temp[3])
#         co = temp[4].replace('\'', '').strip()
#         print(co)
#         oneFigure(x, y, la, ed, co)
# t.done()

# 9
# 用Python对证券行业期刊的文档进行主题词分析，选取的文档集包含2013年到
# # 2016年四年的近2000篇文档，从中提取每年度的主题词序列，其中一组在文件 topic1.txt中，内容如下：
# 2013,客户公司券商服务交易资产投资产品收益
# 2014,收益公司券商客户资产投资交易服务资产证券化
# 2015,公司券商客户服务资产投资债券资产证券化融资融券收益
# 2016,公司客户服务券商资产投资债券管理
# 请利用jieba库分析上述四年的主题词提取有用的信息。
# 1)提取每一年的主题词的个数按照年度顺序显示在屏幕上；显示示例如下：
# 2013:9

# 请在_____处填写一行代码
# 请在……处填写多行代码
# 可修改其他代码

 # 3)分析每一年相比前一年的主题词的差别，在屏幕显示出来；显示示例如下：
# 2014比2013多了主题词：资产证券化；少了主题词：产品
import jieba
def disp_diff(y1, y2, ls1, ls2):
    lessstr = ''
    morestr = ''
    for i in ls1:
        if i not in ls2:
            lessstr = (lessstr + ' ' + i).strip()
    for j in ls2:
        if j not in ls1:
            morestr = (morestr + ' ' + j).strip()
    print('{}比{}多了主题词：{}； 少了主题词:{}'.format(y2, y1, morestr, lessstr))


topics = {}
totaltp = []
counts = {}
sum_count = 0
ttopics = {}

fi = open("topic.txt", "r", encoding='UTF-8')
for line in fi:
    ls = line.strip().split(',')
    ls_key = ls[0]
    ls_val = ls[1]
    ls_val = jieba.lcut(ls_val)
    counts[ls_key] = ls_val
    # print(ls_val)
    for ttp in ls_val:
        totaltp.append(ttp)
fi.close()
# print(counts)
#
# #1 the counts of topics of each year每年的主题数量
# sortedtp = list(counts.items())
# sortedtp.sort(key=lambda x:x[0])
# for year in sortedtp:
#     print(year)
#     print('{}:{}'.format(year[0], counts[year[0]]))

#2.1 the count of topics of 4 years4年主题数
# 2)合计四年来的不同主题词的个数统计，以及每个主题词出现的次数按照主题词次数从大到小 的顺序显示在屏幕上；显示示例如下：
# 4年出现的不同主题词有12个
# 资产：6
# tpset = set(totaltp)
# totaltpcount = len(tpset)
# for i in totaltp:
#     ttopics[i] = ttopics.get(i, 0) + 1
# # lt = list(ttopics.items())
# # lt.sort(key=lambda x: x[-1], reverse=True)
# # print(lt)
# print(tpset)
# print('4年出现的不同主题词有{}个'.format(totaltpcount))
# print(ttopics)
# for i in lt:
#     print('{}{}'.format(i[0],i[1]))
#
# #2.2 the count of each topic in  set of 4 years, from large to little四年一组中每个主题的数量，从大到小
# sortedtp = list(ttopics.items())
# sortedtp.sort(key = lambda x:x[1], reverse=True)
# for tp in sortedtp:
#     print('{}:{}'.format(tp[0], ttopics[tp[0]]))
#
# #3 the difference between every two years每两年的差额
# 3)分析每一年相比前一年的主题词的差别，在屏幕显示出来；显示示例如下：
# 2014比2013多了主题词：资产证券化；少了主题词：产品
print(counts)
for year in range(2013, 2016):
    y1 = str(year)
    y2 = str(year+1)
    ls1 = counts[y1]
    ls2 = counts[y2]
    disp_diff(y1, y2, ls1, ls2)
