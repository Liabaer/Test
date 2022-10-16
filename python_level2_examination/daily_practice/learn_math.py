# -*- coding: utf-8 -*-
import math
import random

# 注意数学类中有些用的是内置的函数，有些是基于math类的，所以有些是直接调用，有些是通过math.的方式调用


# round(a,x) 让a保留x位小数
# print(round(3.144, 2))
# # 第二个参数不填，就四舍五入到整数
# print(round(5.522))
# //是整除
# print(3 // 2)
# # / 是浮点除
# print(3 / 2)


#
# a = 3
# # 表示a的2次方
# a = a ** 2
# print(a)
# 注意 运算符执行的优先级
# 乘方最高，然后先乘除后加减，括号里的先算括号里的
# a = 3 * 4 ** 2 // 2  # 会先计算4的2次方
# print(a)
#
# a = (3 * 4) ** 2 // 2  # 会先计算括号里的
# print(a)
# # #
# # random库采用梅森旋转算法生成伪'随机数'，注意是随机的一个数
# # random返回0-1之间的小数
# print(random.random())
# # # # 返回a-b之间的数字，非整数
print(random.uniform(1, 100))
# # # 返回a-b的整数
# print(random.randint(1, 100))

# # # a的b次方
# print(pow(5, 2))
# # 开根号
# print(math.sqrt(25))

# # 计算绝对值
# print(abs(-5))
# # # 另外一种计算绝对值的方法
# print(math.fabs(-5))

# # 向下取整  floor地板的意思可以这样记
# print(math.floor(5.2))

# # 向上取整 ceil天花板
# print(math.ceil(5.2))
# # 计算5的阶乘 5！
# print(math.factorial(5))

# 角度和弧度关系是：2π弧度 = 360度
# 角度转换为弧度：弧度 = 角度 × (π ÷ 180)
# 弧度转换为角度：角度 = 弧度 ×(180 ÷ π)
# π的值 3.141592657
# print(math.pi)
# # 计算正弦值 sin和cos里面第一个参数输入的是弧度 所以不能sin(60)，要先利用角度转弧度公式计算弧度值
print(math.sin(180 * (math.pi / 180)))  # 等价于我们常见的sin180度 (这个等于0 无限接近0，因为π目前是无理数)
print(math.sin(90 * (math.pi / 180)))  # 等价于我们常见的sin90度 这个等于1
# cos同理
print(math.cos(60 * (math.pi / 180)))  # 等价于我们常见的cos60度 这个等于二分之一，无限接近0.5
