# -*- coding: utf-8 -*-
# 第一题
# 算法平均数蕴含了“重心”的意思，中位数用于概括一组 数据的位置，是高度耐抗的，有个别的极大值或者极小 值，不会引起中位数的变化。
# 在numbers.txt中随机给出了100个人的某月收入（单 位：元)，请参照编程模板，求这些数据的算术平均数 和中位数。本题不支持自动评阅。

# def Arithmetic(numbers):  # 计算算法平均数
#     count = 0
#     num = 0
#     for i in numbers:
#         num += int(i)
#         count += 1
#     avg = int(num) / count
#     return avg
#
#
# def Median(numbers):  # 计算中位数
#     count = 0
#     med = 0
#     number= []
#     for i in numbers:
#         count += 1
#         #一定要先讲字符串专程int类型，才可以排序
#         number.append(int(i))
#     number.sort()
#     if count % 2 != 0:
#         med = number[int(count / 2) + 1]
#     else:
#         med = int(number[int(count / 2)] + number[int(count / 2) + 1]) / 2
#     return med
#
#
# fo = open("numbers.txt", "r", encoding="utf-8")
# ls = []
# for line in fo.readlines():
#     line = line.replace("\n", "")
#     ls.append(line)
#
# print("算术平均数为{}。".format(Arithmetic(ls)))
# print("中位数为{}。".format(Median(ls)))
# eg：
# numbers = ['11', '2', '3']
# numbers.sort()
# print(numbers)
# numbers = list(map(int, numbers)) 直接将字符串的list转换成里面是int的list
# numbers.sort()
# print(numbers)

# eg：replace
# a = 'abcde'
# a = a.replace('a', "1")
# print(a)
# a = "abcdeabc"
# # 将a字符串包含第一个参数的，都转换为第二个参数
# a = a.replace("abc", "gg")
# print(a)


# 第二题
# 按照下面的转换表，要将输入的一个0到100的考分转换成一个用字母表示的分数级别， 输出显
# 示在屏幕上。
# 转换表：
# 0-59:F
# 60-69:D
# 70-79:C
# 80-89:B
# 90-100:A

# def transLevel(x):
    # trans = {0-59:'F', 60-69:'D', 70-79:'C', 80-89:'B', 90-100:'A'}
    # 字典不能使用0-59这种key的写法
    # 这里使用y等于下标的方式找到对应等级
#     trans = '0FFFFFDCBa'
#     if 0 < x <= 100:
#         y = int(x / 10)
#         # 或者 y = x // 10（ // 是整除）
#         if y < 0:
#             y = -1
#         return trans[y]
#     else:
#         return -1
#
#
# x = eval(input())
# y = transLevel(x)
# if y:
#     print('x是:{},分数级别是:{}'.format(x, y))
# else:
#     print('请输入0-100之间的数，请重新运行')
#
#
# 第三题
# 有一个列表stones如下：
# stones=['1901010902,翡翠，21000，
# 1901010903,玛瑙，15000'，
# 1901010900,和田玉，20800'，
# 1901010901,水晶石，18000]
# 第1列是玉石的编号，第2列是玉石名称，第3列是玉石报价。
# 按照玉石编号从小到大显示玉石的编号、名称和报价，并显示价格最低的玉石名称 和价格。
stones = ['1901010902,翡翠,21000', '1901010903,玛瑙,15000', '1901010900,和田玉,20800', '1901010901,水晶石,18000']

std = {}
minp = {}
for s in stones:
    sl = s.split(',')
    key = sl[0]
    key2 = sl[1]
    std[key] = [sl[1], sl[2]]
    minp[key2] = sl[2]

stl = list(std.items())
stl.sort(key=lambda x: x[0])
ml = list(minp.items())
ml.sort(key=lambda x: x[1])
print(ml)
for s in stl:
    print('编号：{}，名称:{}, 报价:{}'.format(s[0], s[1][0], s[1][1]))
print('价格最低的玉石是{},价格是{}'.format(ml[0][0], ml[0][1]))

