# -*- coding: utf-8 -*-

# 选出分数最高的学生,打印输出学生的姓名和分数,中间用英文冒号隔开,示例妙如下

# 在...补全代码块
f_data = open("../data/data.txt", "r", encoding="utf-8")
num = 0
new_name = ''
for i in f_data.readlines():
    # 去掉读取到的字符串后面的回车
    i = i.strip()
    # 使用函数
    name = i.split(":")[0]
    score = i.split(":")[1].split("，")[1]
    # print(name, score)
    if num <= int(score):
        num = int(score)
        new_name = name
print(new_name + ':' + str(num))
f_data.close()

# split函数的运用
# temp = "王一:计算191，340"
# print(temp.split(":"))
# print(temp.split(":")[1])
# print(temp.split(":")[1].split("，"))
# print(temp.split(":")[1].split("，")[1])
