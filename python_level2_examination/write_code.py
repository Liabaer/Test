 # -*- coding: utf-8 -*-
# 以26个小写字母和0~9数字为基础，以用户输入的 数字为种子，随机生成10个8位密码，并将每个密 码在单独一行打印输出。
# 例如输入：125

# 在————————上补充代码
import random


s = input("请输入随机种子：")
ls = []
for i in range(26):
    ls.append(chr(ord('a') + i))
    print('----', ls)
for i in range(10):
    # number_ascci = ord('0') + i
    # chr(number_ascci)
    ls.append(chr(ord('0') + i))
print(ls)
random.seed(s)
for i in range(10):
    for j in range(8):
        # 随机从数组中选一个元素
        print(random.choice(ls), end='')
    # 直接print()是空格
    print()