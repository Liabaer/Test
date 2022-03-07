# -*- coding: utf-8 -*-
# 某班学生评选一等奖学金，学生的1O门主干课程成绩存在附件score.txt中，每行为
# 一个学生的信息，分别纪录了学生学号、姓名以及10门课成绩，格式如下：
# 问题1：给出按总成绩从高到底排序的前10名学生名单，并写入文件candidate0.txt
# 每行纪录一个学生的信息，分别为学生学号、姓名以及10门课成绩。补充，修改编 程模板中的代码完成这些功能。

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

L = []  # L中的元素是学生原始成绩和总成绩
f = open('score(1).txt', encoding='utf-8')  # 此处可多行
score = f.readlines()
# print(score)
# 初始化一个字典用来输出最后结果
res = {}
for i in score:
    # print(i)
    score_sum = 0
    temp = ''
    for j in i.split(' ')[2:12]:
        score_sum += int(j)
        # 用temp来放每个学员的各科成绩
        temp = temp + ' ' + str(j)
        # print(temp)
    # print(i.split(' ')[0]+' '+i.split(' ')[1]+':'+str(score_sum))
    # 这里是放进二维数组的步骤，后续简写了
    # temp.append(score_sum)
    # temp.append(i.split(' ')[0]+' '+i.split(' ')[1])
    # temp.append(score_sum)
    # 这里是放的二维数组简写，lambda的参数x: x[n]，n=-1 只能对 元祖，数组，字符串进行比较
    L.append([i.split(' ')[0]+' '+i.split(' ')[1], str(score_sum)])
    # 将学员的学号，姓名当做字典的key，成绩当成values存入字典
    res[i.split(' ')[0] + ' ' + i.split(' ')[1]] = temp
L.sort(key=lambda x: x[-1], reverse=True)  # 按学生总成绩从大到小排序
print(L)  # 此处可多行
print(res)
# with open("candidate0.txt", "w", encoding="utf-8") as fi:
#     for i in L:
#     # print(str(i))
#         # 根据L.sort对二维数组排序后，用字典的key来根据L的排序放入学科的成绩
#         fi.write("{}{}".format(i[0], res[i[0]]))
#
# 跟上面写法一样的效果，但是性能会差一些，需要每次都打开文件一次再写入数据
# for i in L:
#     # print(str(i))
#     with open("candidate0.txt", "a", encoding="utf-8") as fi:
#         # 根据L.sort对二维数组排序后，用字典的key来根据L的排序放入学科的成绩
#         fi.write("{}{}".format(i[0], res[i[0]]))