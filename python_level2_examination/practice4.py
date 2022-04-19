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
# # 1901010903,玛瑙，15000'，
# # 1901010900,和田玉，20800'，
# # 1901010901,水晶石，18000]
# # 第1列是玉石的编号，第2列是玉石名称，第3列是玉石报价。
# # 按照玉石编号从小到大显示玉石的编号、名称和报价，并显示价格最低的玉石名称 和价格。
# stones = ['1901010902,翡翠,21000', '1901010903,玛瑙,15000', '1901010900,和田玉,20800', '1901010901,水晶石,18000']
#
# std = {}
# minp = {}
# for s in stones:
#     sl = s.split(',')
#     key = sl[0]
#     key2 = sl[1]
#     std[key] = [sl[1], sl[2]]
#     minp[key2] = sl[2]
#
# stl = list(std.items())
# stl.sort(key=lambda x: x[0])
# ml = list(minp.items())
# ml.sort(key=lambda x: x[1])
# print(ml)
# for s in stl:
#     print('编号：{}，名称:{}, 报价:{}'.format(s[0], s[1][0], s[1][1]))
# print('价格最低的玉石是{},价格是{}'.format(ml[0][0], ml[0][1]))

# 第四题
# 取文件 gasconc.txt里记录的不同房间里的二氧化碳气体浓度传感器的数据，第一列 是传感器编号，第二列是房间名称，第三列是浓度值。示例如下：
# GS602:臣卧室1：1500
# GS600:臣室2：1200
# GS610:卫生间：500
# GS620:餐厅：600
# 1)请将数据读入到字典sensor里，以传感器编号为键，气体名称和浓度以列表的形式作为值；在屏幕上按照键值由小到大顺序输出字典sensor的内容。
# 2)建立新的字典gas,l 以房间名称为键，以浓度作为值；在屏幕上按照气体浓度从 大到小排序后，输出gas的内容
# sensor = {}
# gas = {}
# with open('gasconc.txt', 'r', encoding='UTF-8-sig') as f:
#     f_new = f.readlines()
#     for i in f_new:
#         i = i.strip()
#         k = i.split(':')[0]
#         v = i.split(':')[1]+','+i.split(':')[2]
#         new_k = v.split(',')[0]
#         new_v = v.split(',')[1]
#         sensor[k] = v
#         gas[new_k] = new_v
#         # print(i)
#     f.close()
# sensor_l = list(sensor.items())
# sensor_l.sort(key=lambda x: x[0], reverse=True)
# temp = []
# for i in sensor_l:
#     temp.append(i[1].split(',')[0])
#     temp.append(i[1].split(',')[1])
#     print('传感器{}:{}'.format(i[0], temp))
#     temp = []
#
# gas_l = list(gas.items())
# gas_l.sort(key=lambda x: x[-1])
# for i in gas_l:
#     print('{}的浓度是：{}'.format(i[0], i[1]))

# 第五题
# 请利用jieba库分析药方，提取有用的信息。
# ·提取药方中的四个标签及标签后面的内容，用字典medi记录。
# 文件内容示例如下：
# 处方：人参3克，石莲肉12克，莲须3克，麦冬6克，远志6克，芡实6克，甘草3克 功能主治：养心安神，主心肾不交 用法用量：水煎服，每日1剂，日服2次 摘录：《仙拈集》卷二
# 字典内容示例如下（字典顺序可以不一致）：
# {"处方'：'人参3克，石莲肉12克，莲须3克，麦冬6克，远志6克，芡实6克，甘草3克，用法用量'：'水煎服，每日 1剂，日服2次，功能主治：'养心安神，主心肾不交，摘录：·《仙拈集》卷二}
# ·将药方中的【处方】标签对应的处方内容，进行统计分析，计算并在屏幕上显示处方药量的总和，药量最大的药 名及其药量；示例如下：
# 总药量是：39
# 药量最大的药是：石莲肉，药量是：12
# import jieba
#
# fi = open("anshentang.txt", "r", encoding="utf-8")
# medi = {}
# f = fi.readlines()
# for i in f:
#     i = i.strip()
#     temp = i.split('】')[0]
#     n = len(temp)-1
#     k = temp[-n:]
#     v = i.split('】')[1]
#     v = v.strip()
#     medi[k] = v
#     # print(k, v)
# print(medi)
# fi.close()
#
# n = medi['处方']
# cnt = 0
# m = 0
# key = ''
# new_medi = {}
# # 可以 split 分割字符串
# # l = n.split('，')
# # print(l)
# l =[]
# temp = ''
# for i in n:
#     if i != '，':
#         temp += i
#     else:
#         l.append(temp)
#         temp = ''
# if temp != '':
#     l.append(temp)
# print(l)
# for i in l:
#     i = i.strip()
#     k = i.split(' ')[0]
#     v = int(i.split(' ')[1][0:-1])
#     cnt += v
#     if m < v:
#         m = v
#         key = k
#     # new_medi[k] = v
#     # print(k, v)
# print("总药量是：{}".format(cnt))
# print("药量最大的药是：{}，药量是：{}".format(key, m))
# for k, v in new_medi.items():
#     if int(v) == m:
#         print("药量最大的药是：{}，药量是：{}".format(k, v))
#         break

#
# 第六题
# 其中，每行是一个记录，空格分隔多个含义，分别包括日期、时间、温 度、湿度、光照、空气干燥度和操作员姓名。其中，光照处于第5列。
# 统计并输出传感器采集数据中光照部分的最大值、最小值和平均值，所 有值保留小数点后2位，并输出低于平均值的数据个数。
# 然后按照光照 时长进行升序排序，将排序后的结果写入到sensor-data-sort.txt中，新 文件的第一列是操作人姓名，第二列是时间（只精确到分)，第三列是 光照时长。

#
# try:
#     f = open("sensor-data.txt", 'r')
#     fl = f.readlines()
#     max_num = 0
#     min_num = 100
#     avg_num = 0
#     num = 0
#     count = 0
#     low_avg = 0
#     new_list = []
#     for i in fl:
#         i = i.strip()
#         if i == '':
#             continue
#         # 第一问
#         count += 1
#         # 有了float就不用int取整了
#         temp = float(i.split(' ')[4])
#         num += temp
#         if max_num < temp:
#             max_num = temp
#         if min_num > temp:
#             min_num = temp
#         # print(i)
#
#         # 第二问
#         name = i.split(' ')[-1]
#         time = i.split(' ')[1][0:5]
#         # 这样处理不方便排序
#         # new_temp = name + ',' + str(time) + ',' + str(temp)
#         # 如果是上面的写法是这样排序
#         # new_list.sort(key=lambda x: int(x.split(",")[2]))
#         new_temp = [name, time, temp]
#         new_list.append(new_temp)
#     f.close()
#     avg_num = num / count
#     for i in fl:
#         i = i.strip()
#         if i == '':
#             continue
#         temp = float(i.split(' ')[4])
#         if temp < avg_num:
#             low_avg += 1
#     print("传感器采集数据中光照部分的最大值:{:.2f}、最小值:{:.2f}和平均值:{:.2f},低于平均值的数据个数{}".format(max_num, min_num, avg_num, low_avg))
#     # print(new_list)
#     new_list.sort(key=lambda x: x[-1])
#     print(new_list)
#     new_f = open('sensor-data-sort.txt', 'w')
#     for i in new_list:
#         new_f.write('{}\n'.format(i))
#     new_f.close()
# except:
#     print("文件打开错误")


# 第七题
# 从data.txt文件读入一篇文章，用jieba库的函数lcut的全模式做分词。
# 问题1：输 出词汇长度为2的词出现的总数，并且输出前10名出现次数最多的词汇，按照降序 输出。
# 问题2：将文件里面的内容反转写入到新的文件data-out.txt中

import jieba
dk = {}
temp = [':', ',', '（', '）', '.', ' ', '\n', '-', '，', '「', '」', '？', '：', '；', '。', '、']
two_cnt = 0
f = open('data-in.txt', 'r')
fr = f.readlines()
fn = open('data-out.txt', 'w')
new_str = ''
for i in fr:
    new_str += i
    i = i.strip()
    m = jieba.lcut(i)
    for j in m:
        if j in temp:
            continue
        else:
            if len(j) == 2:
                two_cnt += 1
            dk[j] = dk.get(j, 0) + 1
        # print(j)
    # print(i)
fn.write(new_str[::-1])
fn.close()
dl = list(dk.items())
dl.sort(key=lambda x: x[-1], reverse=True)
res = []
for i in dl[0:10]:
    res.append(i[0])
print("词汇长度为2的词出现的总数:{},前10名出现次数最多的词汇有{}".format(two_cnt, res))
f.close()

