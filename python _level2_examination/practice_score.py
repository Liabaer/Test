# -*- coding: utf-8 -*-
# 某班学生评选一等奖学金，学生的1O门主干课程成绩存在附件score.txt中，每行为
# 一个学生的信息，分别纪录了学生学号、姓名以及10门课成绩，格式如下：
# 从这些学生中选出奖学金候选人。条件如下：
# 问题1：总成绩排名在前10名；
# 问题2：全部课程及格( 成绩大于等于60)。

# 问题1：给出按总成绩从高到底排序的前10名学生名单，并写入文件candidate0.txt
# 每行纪录一个学生的信息，分别为学生学号、姓名以及10门课成绩。补充，修改编 程模板中的代码完成这些功能。

# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

# L = []  # L中的元素是学生原始成绩和总成绩
# f = open('score(1).txt', encoding='utf-8')  # 此处可多行
# score = f.readlines()
# # print(score)
# # 初始化一个字典用来输出最后结果
# res = {}
# for i in score:
#     # print(i)
#     score_sum = 0
#     temp = ''
#     for j in i.split(' ')[2:12]:
#         score_sum += int(j)
#         # 用temp来放每个学员的各科成绩
#         temp = temp + ' ' + str(j)
        # print(temp)
    # print(i.split(' ')[0]+' '+i.split(' ')[1]+':'+str(score_sum))
    # 这里是放进二维数组的步骤，后续简写了
    # temp.append(score_sum)
    # temp.append(i.split(' ')[0]+' '+i.split(' ')[1])
    # temp.append(score_sum)
    # 这里是放的二维数组简写，lambda的参数x: x[n]，n=-1 只能对 元祖，数组，字符串进行比较
    # L.append([i.split(' ')[0]+' '+i.split(' ')[1], str(score_sum)])
    # 将学员的学号，姓名当做字典的key，成绩当成values存入字典
#     res[i.split(' ')[0] + ' ' + i.split(' ')[1]] = temp
# L.sort(key=lambda x: x[-1], reverse=True)  # 按学生总成绩从大到小排序
# print(L)  # 此处可多行
# print(res)
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

#
# 问题2：读取文件candidate0.txt,从中选出候选人，并将学号和姓名写入文件 candidate.txt,格式如下：
# 从这些学生中选出奖学金候选人。条件如下：
# 问题1：总成绩排名在前10名；
# 问题2：全部课程及格( 成绩大于等于60)。
# 1010112161722张三
# 1010112161728李四
# 补充修改模板，完成这一功能。请注意，问题2使用的candidate0.txt是你回答问题 1所生成的文件，
# 附件里附带的文件是方便你学习理解给出的正确答案，正式考试的 时候是不给你这个文件的，
# 需要你自己生成，一旦你生成的文件有错误，问题2， 你也就无缘得分了。

'''
输入文件 ： candidate0.txt
输出文件 ： candidate.txt
'''

f = open('candidate0.txt', encoding='utf-8')
f = f.readlines()
temp = []
res = []
# print(f)
for i in f:
    temp = i.split(' ')[2:12]
    # print(i)
    j = 0
    flag = True
    while j < len(temp):
        # print(temp[j])
        # print(flag)
        if int(temp[j]) < 60:
            flag = False
            j = j + 1
            break
        j = j + 1
    if flag:
        f = open("candidate.txt", 'a', encoding="utf-8")
        # print(temp)
        # 这行代码是无效的， 但是为了提醒自己的思路是当flag=True时，可以拿到temp，利用temp来取出满足条件的值
        if temp == i.split(' ')[2:12]:
            # 测试代码
            res.append(i.split(' ')[0:2])
            # f.write("{} {}\n".format(i.split(' ')[0], i.split(' ')[1]))

