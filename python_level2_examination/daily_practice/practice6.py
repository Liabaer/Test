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
# import jieba
# def disp_diff(y1, y2, ls1, ls2):
#     lessstr = ''
#     morestr = ''
#     for i in ls1:
#         if i not in ls2:
#             lessstr = (lessstr + ' ' + i).strip()
#     for j in ls2:
#         if j not in ls1:
#             morestr = (morestr + ' ' + j).strip()
#     print('{}比{}多了主题词：{}； '
#           '少了主题词:{}'.format(y2, y1, morestr, lessstr))
#
#
# topics = {}
# totaltp = []
# counts = {}
# sum_count = 0
# ttopics = {}
#
# fi = open("topic.txt", "r", encoding='UTF-8')
# for line in fi:
#     ls = line.strip().split(',')
#     ls_key = ls[0]
#     ls_val = ls[1]
#     ls_val = jieba.lcut(ls_val)
#     counts[ls_key] = ls_val
#     # print(ls_val)
#     for ttp in ls_val:
#         totaltp.append(ttp)
# fi.close()
# print(counts)
#
# #1 the counts of topics of each year每年的主题数量
# sortedtp = list(counts.items())
# sortedtp.sort(key=lambda x:x[0])
# for year in sortedtp:
#     print(year)
#     print('{}:{}'.format(year[0], counts[year[0]]))

# 2.1 the count of topics of 4 years4年主题数
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
# print(counts)
# for year in range(2013, 2016):
#     y1 = str(year)
#     y2 = str(year+1)
#     ls1 = counts[y1]
#     ls2 = counts[y2]
#     disp_diff(y1, y2, ls1, ls2)

# # 10
# 从键盘输入5个整数，用逗号隔开，对这5个整数从小到大排序，并输出结果到屏幕 上。
# 编写一个冒泡排序的函数BubbleSort(numbers),并调用该函数完成排序。示 例如下：  20,23,34,52,11

# 请在_____处填写一行代码
# 请在….处填写多行代码
# 不可修改其他代码
# def BubbleSort(numbers):
#     """
#     冒泡排序
#     :param numbers: 传入要排序的数组
#     :return: 返回排序后的数组
#     """
#     for i in range(len(numbers)):
#         temp = ''
#         for j in range(len(numbers) - i - 1):
#             if numbers[j] > numbers[j + 1]:
#                 temp = numbers[j]
#                 numbers[j] = numbers[j + 1]
#                 numbers[j + 1] = temp
#     return numbers

#
# print("请输入5个整数，用逗号隔开：")
# numbers = input()
# # numls = numbers.split(',') 转换成int来比较，避免使用了ascii码排序
# numls = [int(i) for i in numbers.split(",")]
# sortednum = BubbleSort(numls)
# print(','.join(str(i) for i in sortednum))
#
# 11
# 这里给出一个《天龙八部》的网络版本，文件名为“天龙八 部-网络版txt"。
# 问题1：请编写程序，对这个《天龙八部》文本中出现的汉字和标点符号进行统计，
# 字符与出现次数之间用冒号：分隔，输出保存到“天龙八部-汉字统计.xt”文件中，参 考格式如下（注意，不统计空格和回车字符）：
# fi = open("天龙八部-网络版.txt", "r", encoding='utf-8')
# fo = open("天龙八部-汉字统计.txt", "w", encoding='utf-8')
# txt = fi.read()
# d = {}
# for c in txt:
#     d[c] = d.get(c, 0) + 1
# del d[' ']
# del d['\n']
# ls = []
# print(d)
# for i in d:
#     ls.append('{}:{}'.format(i, d[i]))
# print(ls)
# fo.write(",".join(ls))
# fo.close()
# fi.close()

# # 2对《天龙八部》文本中出现的中文词语进行统计，采用jieba 库分词，词语与出现次数之间用冒号：分隔，输出保存到“天龙八部-词语统计.xt"文 件中。
# import jieba
# fi = open("天龙八部-网络版.txt", "r", encoding='utf-8')
# fo = open("天龙八部-词语统计.txt", 'w', encoding='utf-8')
# txt = fi.read()
# words = jieba.lcut(txt)
# d = {}
# for w in words:
#     d[w] = d.get(w, 0) + 1
# del d[' ']
# del d['\n']
# ls = []
# for key in d:
#     ls.append('{}:{}'.format(key,d[key]))
# fo.write(','.join(ls))
# fo.close()
# fi.close()

# 12
# 编写Python程序输出一个具有如下风格效果的文本，用作文本进度条样式，部分代 码如下，填写空格处。
# 前三个数字，右对齐；后面字符，左对齐
# 文本中左侧一段输出N的值，右侧一段根据N的值输出等号，中间用@分隔，等号 个数为N与5的整除商的值，例如，当N等于10时，输出2个等号。

# N = eval(input())
# print('{}@{}'.format(N, "=" * (N//5)))

# # 13
# 请用户输入字符串，判断输入的若干字符串是否是回文串，并显示判断结果；然后提
# # 示用户输入Y'则继续判断，否则跳出循环结束判断。
# flag = "Y"
# while flag:
#     print("请输入一个字符串：")
#     x = input()
#     if x[::-1] == x:
#         print(x + "是一个回文串")
#     else:
#         print(x + "不是一个回文串")
#     print("如果继续判断字符串是否是回文串，请输入Y：")
#     x = input()
#     if x == 'Y':
#         flag = "Y"
#     else:
#         break

# 14
##求出一组数中的众数及出现频率
# ls = [1080,750,1080,750,1080,850,960,2000,1250,1630,1080,1800,1080,2100,1080,1450,2500,560,1080,560]
# counts ={}
# for num in ls:
#     counts[num] = counts.get(num,0) + 1
# items = list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)
# num,count = items[0][0],items[0][1]
# print("众数为{},出现频率为{}。".format(num,count))

# 15
# 根据PM2.5检测网的空气质量新标准，24小时平均值标准值分布如下：
# 如果输入内容为24小时PM2.5平均值标准值，输出内容为"空气质量等级"。如果输
# 入的不是数值，输出为"输入数值有误"。
# s = ""
# try:
#     n = eval(input(""))
# except:
#     s = "输入数值有误"
#
#
# def isgood(n):
#     global s
#     if 0 <= n < 35:
#         s = "空气等级质量为优"
#     elif 35 <= n < 75:
#         s = "空气等级质量为良"
#     elif 75 <= n < 115:
#         s = "空气等级质量为轻度污染"
#     elif 115 <= n < 150:
#         s = "空气等级质量为轻中度污染"
#     elif 150 <= n < 250:
#         s = "空气等级质量为轻重度污染"
#     elif 250 <= n:
#         s = "空气等级质量为轻严重污染"
#     else:
#         s = "输入数值有误"
#     print(s)
#
#
# if s == "输入数值有误":
#     print("输入数值有误")
# else:
#     isgood(n)

# 16
# data-infomation.txt是一个来源于网上的技术信息资料。
# 问题1：用Python语言中文分词第三方库jieba对文件data.txt进行分词，
# 并选择长度大于等于3个字符的关键词，写入文件out1.txt,每行一个关 键词，各行的关键词不重复，输出顺序不做要求，例如：

# 注意：提示框架代码可以任意修改，以完成程序功能为准
# import jieba
# f = open('out1.txt','w')
# fi = open("data-infomation.txt","r")
# fd = fi.readlines()
# ls = []
# for i in fd:
#     i = i.strip()
#     temp = jieba.lcut(i)
#     print(temp)
#     for j in temp:
#         if len(j) >= 3:
#             ls.append(j)
# ls = set(ls)
# for i in ls:
#     f.write('{}\n'.format(i))
# fi.close()
# f.close()

# 问题2：对文件data-infomation.txt进行分词，对长度不少于3个字符的 关键词，统计出现的次数，
# 按照出现次数由多到少的顺序输出到文件 out2txt,每行一个关键词及其出现次数，例如：
# import jieba
# fi = open("data-infomation.txt","r")
# fo = open("out2.txt","w")
# fd = fi.readlines()
# ls = []
# for i in fd:
#     i = i.strip()
#     temp = jieba.lcut(i)
#     print(temp)
#     for j in temp:
#         if len(j) >= 3:
#             ls.append(j)
# ld = {}
# for i in ls:
#     ld[i] = ld.get(i, 0)+1
# l = list(ld.items())
# l.sort(key=lambda x: x[1], reverse=True)
# for i in l:
#     fo.write('{}:{}\n'.format(i[0],i[1]))
# fi.close()
# fo.close()


# 17
# 这里有一个中文文本片段：“今天北京有个好天气，大家一起去爬山。
# "该句子分上 下两部分，以逗号和句号分隔。请对该句子进行分词，并以8为随机种子，在上下半 句分别重新排列组合词语，" \
# "并组合输出10种不重复的可能。
# import jieba
# import random
# s = "今天北京有个好天气，大家一起去爬山。"
# k = s.find('，')
# s1 = jieba.lcut(s[0:k])
# s2 = jieba.lcut(s[k+1:-1])
# # random.seed(8)
# lines = []
# while True:
#     line = ""
#     random.shuffle(s1)
#     random.shuffle(s2)
#     # 这里不能直接append s1，s2
#     a = ''.join(s1.copy())
#     b = ''.join(s2.copy())
#     temp = a+','+b
#     lines.append(temp)
#     if len(lines) == 10:
#         break
# # print(lines)
# # print('\n'.join(lines))
# f = open("句子组合.txt", "w")
# f.write('\n'.join(lines))
# f.close()

# 18
# 用字典和列表型变量完成某课程的考勤记录统计。某班有20名同学，名单由 name.txt给出，某课程2次考勤数据由文件1.csv、2.csv。
# f = open("name-1.txt", 'r')
# fr = f.readlines()
# lname = []
# for i in fr:
#     lname.append(i)
# ld = {}
# for i in range(1, 3):
#     fo = open("data-" + str(i) + ".csv", "r", encoding="utf-8")
#     fl = fo.readlines()
#     for j in fl[1::]:
#         j = j.strip()
#         j = j.split(',')[0]
#         ld[j] = ld.get(j, 0) + 1
#     fo.close()
# for k in ld:
#     if ld[k] >= 2:
#         print('全勤的同学有:{}'.format(k))
# f.close()

# 19
# 使用turtle库绘制钢琴键示意图形，效果如下图所示。
# import turtle as t
# t.setup(500, 300)
# t.penup()
# t.goto(-180, -50)  #将画笔移动到绝对位置(-180,-50)处
# t.pendown()   #画笔落下
# def Drawrect():
#     t.fd(40)
#     t.left(90)
#     t.fd(120)
#     t.left(90)
#     t.fd(40)
#     t.left(90)
#     t.fd(120)
#     t.penup()
#     t.left(90)
#     t.fd(42)
#     t.pendown()
# for i in range(7):
#     Drawrect()
# t.penup()
# t.goto(-150,-0) #将画笔移动到绝对位置(-150,-0)处
# t.pendown() #画笔落下
# def DrawRectBlack():
#     t.color('black')
#     t.begin_fill()
#     t.fd(30)
#     t.left(90)
#     t.fd(70)
#     t.left(90)
#     t.fd(30)
#     t.left(90)
#     t.fd(70)
#     t.end_fill()
#     t.penup()
#     t.left(90)
#     t.fd(40)
#     t.pendown()
# DrawRectBlack()
# DrawRectBlack()
# t.penup()
# t.fd(48)
# t.pendown()
# DrawRectBlack()
# DrawRectBlack()
# DrawRectBlack()
# t.hideturtle()
# t.done()

# 20
# 使用turtle库绘制八角星形，效果如下图所示
# import turtle as t
# t.colormode(255)
# t.color(255,215,0)  #设置颜色取值为金色（255,215,0）
# t.begin_fill()
# for x in range(8):
#     t.fd(100)
#     t.left(225)
# t.end_fill()
# t.hideturtle()
# t.done()

# 21
# # 使用turtle库绘制简单城市剪影图形，效果如下图所示。
# import turtle
# # 设置绘画框的大小
# turtle.setup(800,300)
# turtle.penup()
# turtle.fd(-350)
# turtle.pendown()
# def DrawLine(i):
#     for angle in [0,90,-90,-90,90]:
#         turtle.left(angle)
#         turtle.fd(i)
# for i in [20,30,40,50,40,30,20]:
#     DrawLine(i)
# turtle.hideturtle()
# turtle.done()

# 22
# 1949年4月23日，中国人民解放军午夜解放南京，毛泽东同志在清晨获得消息后写 下《七律人民解放军占领南京》，全文如下：
# 问题1：这是一段由标点符号分隔的文本，请编写程序，以标点符号为分隔，将这段 文本转换为诗词风格。
# 问题一输出：
# 每行30个字符，诗词居中，每半句一行，去掉所有标点。输出到文件”七 律.txt"。
# s = "钟山风雨起苍黄，百万雄师过大江。\
# 虎踞龙盘今胜昔，天翻地覆慨而慷。\
# 宜将剩勇追穷寇，不可沽名学霸王。\
# 天若有情天亦老，人间正道是沧桑。"
#
# fo = open("七律.txt", 'w')
# s = s.split('。')
# for i in s:
#     i = i.strip()
#     i = i.split('，')
#     print(i)
#     for j in i:
#         fo.write('{:^30}\n'.format(j))
# fo.close()

# 问题2 输出全文的翻转形式。
# s = "钟山风雨起苍黄，百万雄师过大江。\
# 虎踞龙盘今胜昔，天翻地覆慨而慷。\
# 宜将剩勇追穷寇，不可沽名学霸王。\
# 天若有情天亦老，人间正道是沧桑。"
# ls = []
# for i in range(0, len(s), 8):
#     # 这里切片要同时处理开头和结尾，动态存到ls里去
#     temp = s[i:i+7]
#     ls.append(temp)
# print(ls)
# ls.reverse()
# print(ls)
# n = 0
# for item in ls:
#     n = n + 1
#     if n%2 != 0:
#         print(item, end="，")
#     else:
#         print(item, end="。\n")

# 23
# 文件sweb.html保存了一个网页的源代码，其中，"href="引导后面会有一个URL链 接，
# 例如：href="http:news.sina.com.cn/feedback/post.html",其中，有一种链接前后都有空格，且双引号内以“http:"开头。
# 请编写程序，解析这个文件，提取出现符合上述特征的URL链接，每个链接一行，
# 保存到“text-urls.txt"文件中，格式如下：

# fi = open("sweb.html", 'r')
# fo = open("text-urls.txt" , 'w')
# txt = fi.read()
# ls = txt.split(' ')
# # print(ls)
# urls = []
# for item in ls:
#     item = item.strip()
#     try:
#         k = item.index('href="http')
#         l = item.index('"', k+6)
#         temp = item[k+6:l]
#         if temp != '':
#             urls.append(temp)
#         # print(temp)
#     except:
#         continue
# print(urls)
# for item in urls:
#     fo.write(item + "\n")
# fi.close()
# fo.close()

# 24
# 使用python实现冒泡排序法。
# 注释：冒泡排序(BubbleSort)的基本概念是：依次比 较相邻的两个数，将小数放在前面，大数放在后面。即 在第一趟：首先比
# 较第1个和第2个数，将小数放前，大数放后。然后比较 第2个数和第3个数，将小数放前，大数放后，如此继 续，直至比较最后两
# 个数，将小数放前，大数放后。输出格式打印逗号拼接 的字符串
#
# #python实现冒泡排序法
# ls = [23,41,32,12,56,76,35,67,89,44]
# def bub_sort(s_list):
#     for i in range(len(s_list)-1):
#         for j in range(len(s_list)-1-i):
#             if s_list[j] > s_list[j+1]:
#                 s_list[j],s_list[j+1] = s_list[j+1],s_list[j]
#     return s_list
# bub_sort(ls)
# print(','.join(str(i) for i in ls))

# # 25
# draw.py是一个turtle绘图的Python程序，内部采用了import turtle模式引入 turtle库。
# 以该文件为输入，修改源代码，输出对应的import turtle ast模式源代码，名称为draw2.py,要求draw2.py运行结果与draw.py一致。
# fi = open("draw(1).py", "r", encoding='utf-8')
# fo = open("draw2.py", "w", encoding='utf-8')
# txt = fi.read()
# txt = txt.replace('import turtle', 'import turtle as t')
# txt = txt.replace('turtle.', 't.')
# # print(txt)
# fo.write(txt)
# fi.close()
# fo.close()

# 26
# 使用无限循环方式从键盘上接收输入姓名，将姓名保存
# # 在一个列表中，如果输入了Q键结束输入。最终输出的格式为name1,name2,name3,name4
# ls = []
# s = input("")
# while True:
#     if s == "Q":
#         break
#     for c in s:
#         if c == "Q":
#             break
#     s = input("")
#     ls.append(s)
# print('，'.join(i for i in ls))

# 27
# 经常会有要求用户输入整数的计算需求，但用户未必一定输入整数。为了提高用户 体验，
# 编写getInput(0函数处理这样的情况。请补充如下代码，如果用户输入整 数，
# 则直接输出整数并退出，如果用户输入的不是整数，则要求用户重新输入，直 至用户输入整数为止。

# def getInput():
#     try:
#         txt = input()
#         while eval(txt) != int(txt):
#             txt = input()
#     except:
#     在函数内部调用自己这个函数，叫递归
#     ps:启发式搜索也是利用的递归的写法，然后一直自己调用自己直到他找到最优解，然后再返回。
#         return getInput()
#     return eval(txt)
# print(getInput())

# # 28
# 编写代码完成如下功能：
# (1)建立字典d,包含内容是："数学"：101，"语文"：202，"英语"：203，"物理"：204， "生物"：206。
# (2)向字典中添加键值对"化学"：205。
# (3)修改"数学"对应的值为201。
# (4)删除"生物"对应的键值对。
# (5)打印字典d全部信息，参考格式如下（注意，其中冒号为英文冒号，逐行打 印)：
# d = {"数学":101,"语文":202,"英语":203,"物理":204,"生物":206}
#
# d["化学"] = 205
# d["数学"] = 201
# del d["生物"]
# for key in d:
#     print('{}:{}'.format(key, d[key]))

# 29
# 以论语中一句话作为字符串变量S,补充程序，分别输出字符串s中汉字和标点符号的个数。
# s = "学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
# n = 0  # 汉字个数
# m = 0  # 标点符号个数
# m = s.count(',')+ s.count('?') #  m = len([i for i in s if i == ',' or i == '?'])
# n = len(s)-m
# print("字符数为{}，标点符号数为{}。".format(n, m))

# 30
# 获得输入正整数N,判断N是否为质数，如果是则输出True,否则输出
# False。本题不考虑输入异常情况。
#
# N = eval(input())
# if N == 1:
#     flag = False
#     print(flag)
# else:
#     flag = True
#     for i in range(2, N):
#         if N % i == 0:
#             flag = False
#             break
#     print(flag)

# 31
# # 输出如下数列在1000000以内的值，以逗号分隔：k(0)=1,k(1)=2,k(n =k(n-1)2+k(n-2)2,其中，k(n)表示该数列。
# a, b = 1, 2
# ls = []
# ls.append(str(a))
# ls.append(str(b))
# for i in range(2,1000000):
#     temp = 0
#     # 这里是公式 太大的数字str无法计算
#     temp = int(ls[i-1]) * int(ls[i-1]) + int(ls[i-2]) * int(ls[i-2])
#     ls.append(str(temp))
#     # 当temp大于1000000时，结束循环
#     if temp > 100000:
#         break
# print(",".join(ls))

# 32
# 使用turtle库绘制如下图的类斯洛克图形，效果如下图所示。
# import turtle
# #绘制边长为20的圆形
# def drawCircle():
#     turtle.pendown()
#     turtle.circle(20)
#     turtle.penup()
#     turtle.fd(40)
# #绘制n层图形
# def drawRowCircle(n):
#     for j in range(n, 1, -1):
#         for i in range(j):
#             drawCircle()
#         turtle.fd(-j*40-20)
#         turtle.right(90)
#         turtle.fd(40)
#         turtle.left(90)
#         turtle.fd(40)
#     drawCircle()
# drawRowCircle(5)
# turtle.hideturtle()
# turtle.done()

# 33
# # 使用turtle库绘制由边长为100像素的菱形构成的六角雪花形状，效果如下图所示。
# import turtle
# def Draw():
#     turtle.begin_fill()
#     turtle.fd(100)
#     turtle.left(60)
#     turtle.fd(100)
#     turtle.left(120)
#     turtle.fd(100)
#     turtle.left(60)
#     turtle.fd(100)
#     turtle.end_fill()
# for i in range(3):
#     turtle.fillcolor('green')
#     Draw()
# turtle.left(60)
# for i in range(3):
#     turtle.fillcolor('blue')
#     Draw()
# turtle.hideturtle()
# turtle.done()

# 34
# 使用turtle库的绘制十二个花瓣的图形，效果如下图所示
# import turtle
# turtle.fillcolor('yellow')
# turtle.begin_fill()
# for i in range(12):
#     turtle.circle(100, -90)
#     turtle.right(120)
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()

# 35
# 软文的诗词风将原有文章根据标点符号重新切分为短语并居中排版，对小屏幕阅读十分有 利。使用程序将普通文章变成软文的诗词风十分有趣。
# txt = '''人生得意须尽欢，莫使金樽空对月。\
# 天生我才必有用，千金散尽还复来。'''
# # 宽度
# linewidth = 30
#
# # 去除标点
# def lineSplit(line):
#     l = ["'","。","，"]
#     temp = ''
#     for i in line:
#         if i in l:
#             continue
#         else:
#             temp+=i
#     return temp
# # 打印答案
# def linePrint(line):
#     global linewidth
#     print('{0:^{1}}'.format(line, linewidth))
#
# newlines = lineSplit(txt)
# for i in range(0, len(newlines), 7):
#     linePrint(newlines[i:i+7])

# 36
# 给定一个整数数字0x1010，请依次输出Python语言中十六进制、十进制、八进制 和二进制表示形式，使用英文逗号分隔。
# n = 0x1010
# print('{},{},{},{}'.format(hex(n),int(n), oct(n),bin(n)))

# 37
# 获得用户输入的以逗号分隔的3个正整数，记为a、b、c,以a为起始数 值，b为步长，c为数字的个数，
# 产生一个递增的等差数列，将这个数列 以列表格式输出，请补充横线处代码。示例如下： 等比的规律就是相邻的2个数之间的倍数为q。  等差数列就是相邻的2个数之间的差为d。
# a,b,c = eval(input())
# ls = []
# for i in range(int(c)):
#     ls.append(a + (i-1)*b)
# print(ls)

# # 38
# 使用字典和列表型变量完成村长选举。某国家有40名有选举权和被选举权的候选 人，名单在附件name.txt中，
# 从这40名候选人中选出一人当总统，40人的投票信息 由附件vote.txt中给出，每行是一张选票的信息，有效票中得票最多的候选人当选。
# 问题1：请从vote.txt中筛选出无效票写入文件vote1.txt。有效票的含义是：选票中只 有一个名字且该名字在name.txt文件列表中，
# 不是有效票的票称之为无效票。
#
# f=open("data-name.txt")
# names=f.readlines()
# f.close()
# f=open("vote-name.txt")
# votes=f.readlines()
# f.close()
# D={}
# NUM=0
# for vote in votes:
#     num = len(vote.split())
#     print(vote[:-1])  #-1是取不到的，所以最后一个回车就被去掉了
#     if num==1 and vote in names:
#         D[vote[:-1]]=D.get(vote[:-1],0)+1
#         NUM+=1
#     else:
#         with open("vote2.txt","a+",encoding="utf-8") as fi:
#             fi.write("{}".format(vote[:-1]))
# print(D)

# 2使用字典和列表型变量完成总统选举。某国家有40名有选举权和被选举权的候选 人，名单在附件name.txt中，
# 从这40名候选人中选出一人当总统，40人的投票信息 由附件vote.txt中给出，每行是一张选票的信息，有效票中得票最多的候选人当选。
# f=open("data-name.txt")
# names=f.readlines()
# f.close()
# f=open("vote-name.txt")
# votes=f.readlines()
# f.close()
# D={}
# NUM=0
# for vote in votes:
#     num = len(vote.split())
#     if num==1 and vote in names:
#         D[vote[:-1]]=D.get(vote[:-1],0)+1
#         NUM+=1
# l=list(D.items())
# l.sort(key=lambda s:s[1], reverse=True)
# print(l)
# name=l[0][0]
# score=l[0][1]
# print("有效票数为：{} 当选总统为:{}，票数为：{}".format(NUM, name, score))

# 39
# 键盘输入小明学习的课程名称及考分等信息，信息间采用空格分隔，每个课程一 行，空行回车结束录入，示例格式如下：
# 数学90
# 语文95
# 英语86
# 物理84
# 生物87
# 屏幕输出得分最高的课程以及成绩，得分最低的课程及成绩，以及平均分（保留2位 小数)
# 注意，其中逗号为英文逗号，格式如下；
# 最高分课程是语文95，最低分课程是物理84，平均分是88.40
# 注意：题目测试用例为循环读入

data = input()  # 课程名 考分
d = {}
while data:
    if data == ' ':
        break
    else:
        temp = data.split(' ')
        d[temp[0]] = temp[1]
    data = input()
num = 0
cnt = len(d)
for key in d:
    num += int(d[key])
ld = list(d.items())
ld.sort(key=lambda x: x[1], reverse=True)
print(ld)
print(
    "最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(ld[0][0], ld[0][1], ld[len(ld) - 1][0], ld[len(ld) - 1][1], num / cnt))
