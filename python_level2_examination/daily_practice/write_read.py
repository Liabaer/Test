# -*- coding: utf-8 -*-

# 读取data.txt,输出学生的姓名和分数到文件 studs.txt,每行一条记录,姓名和分数用英文冒号隔 开:
# 在...补充代码块

# 同级目录就可以直接读取，不需要加路径
f_data = open("../data/data.txt", "r", encoding="utf-8")
f_studs = open("../data/studs.txt", "w", encoding="utf-8")

temp = ''

for temp in f_data.readlines():
    # 去掉读取到的字符串后面的回车
    temp = temp.strip()
    # 使用函数
    # name = i.split(":")[0]
    # score = i.split(":")[1].split("，")[1]
    # print(name, score)
    name = ''
    score = ''
    flagA = False
    flagB = False
    # print(temp)
    for i in temp:
        if i == ':':
            flagA = True
            continue
        if i == '，':
            flagB = True
            continue
        if flagA == False:
            name = name + i
            continue
        if flagB:
            score = score + i
    print(name + ":" + score)
    f_studs.write(name + ":" + score + '\n')
f_data.close()
f_studs.close()
