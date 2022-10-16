# -*- coding: utf-8 -*-
import random

# seed，设定随机算法的随机分布率，一半会默认，题目不指定，不会用，仅仅只是设置随机算法的参数
# seed()没有参数时，每次生成的随机数是不一样的，而当seed()有参数时，每次生成的随机数是一样的，同时选择不同的参数生成的随机数也不一样
# random.seed(25)

# 随机一个0到1的范围的小数
a = random.random()
# print(a)
#
# # # 随机a到b之间的整数
# print(random.randint(1, 100))
# #
# # 随机从数组中选一个元素
s = ['a', 'b', 'c']
# print(random.choice(s))

# # 将数组顺序打乱
# random.shuffle(s)
# print(s)

# # 随机从数组中取n个元素
ss = random.sample(s, 2)
print(ss)
