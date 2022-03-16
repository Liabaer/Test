# -*- coding: utf-8 -*-
# 在横线处填写代码，完成如下功能。
# time库是Python语言中与时间处理相关的标准 库，time库中ctime0函数能够将一个表示时间的 浮点数变成人类可以理解的时间格式

# 在————————上补充代码   1519181231
import time

t = input("请输入一个浮点数信息：")
s = time.ctime(int(t))
ls = s.split()
print(ls)
print(ls[3].split(':')[0])
