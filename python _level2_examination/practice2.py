# -*- coding: utf-8 -*-
# 模板中给出的代码是本题目的提示框架，其中代码可以任意修改。请在该文件中删 除横线，编写代码，以实现一下功能：
# 键盘输入小明学习的课程名称及考分等信息，信息间采用空格分隔，每个课程一 行，空行回车结束录入，示例格式如下：
# 数学90
# 语文95
# 英语86
# 物理84
# 生物87
# 屏幕输出得分最高的课程以及成绩，得分最低的课程及成绩，以及平均分（保留2位 小数)
# 注意，其中逗号为英文逗号，格式如下；
# 最高分课程是语文95，最低分课程是物理84，平均分是88.40

data = input()  # 课程名 考分
score = 0
count = 0

max_score = 0
max_name = ''
min_score = 0
min_name = ''
dict_score = {}
while data:
    if data[0:2] not in dict_score:
        dict_score[data[0:2]] = data[2:4]
    data = input()
print(dict_score)
for k, v in dict_score.items():
    count += 1
    score += int(v)
    avg = score/count
    if int(v) > max_score:
        max_score = int(v)
        max_name = k
    if min_score == 0:
        min_score = int(v)
    if int(v) < min_score:
        min_score = int(v)
        min_name = k
# print(min_name,min_score, max_name, max_score, avg)
print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(min_name, max_score, min_score, min_score, avg))