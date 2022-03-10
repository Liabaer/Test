# -*- coding: utf-8 -*-
# 在右侧的答题模板中，在省略号处填写一行或多行代码，完成如下功能。在已定义 好的字典Pdict里有一些人名及其电话号码。
# 请用户输入一个人的姓名，在字典中 查找该用户的信息，如果找到，生成一个范围在1000到9999之间的四位数字的验 证码，
# 并将名字、电话号码和验证码输出在屏幕上，如示例所示。如果查找不到该 用户信息，则显示“对不起，您输入的用户信息不存在。“示例如下：

import random

random.seed(2)

pdict = {'Alice': ['123456789'],
         'Bob': ['234567891'],
         'Lily': ['345678912'],
         'Jane': ['456789123']}

name = input('请输入一个人名:')
code = random.randint(1000, 9999)
flag = True
for k, v in pdict.items():
    if name == k:
        flag = True
        print("{} {} {}".format(k, v[0], code))
        break
    else:
        flag = False
if not flag:
    print('对不起，您输入的用户信息不存在。')
