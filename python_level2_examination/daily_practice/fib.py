# -*- coding: utf-8 -*-
#
# 第一题
# 根据斐波那契数列的定义，F(0)=0,F（1)=1,F(n)=F(n-1)+F(n-2)(n>=2) 输出不大于100的序列元素。
# 例如：屏幕输出实例为：
# # 0,1,1,2,3,.(略)
# a, b = 0, 1
# while a <= 100:
#     print(a, end=',')
#     a, b = b, a+b

# # 斐波那契数列
fb = []
# a = 0
# b = 1
# fb.append(a)
# fb.append(b)
# cnt = 2
# while cnt < 100:
#     temp = a + b
#     fb.append(temp)
#     a = b
#     b = temp
#     cnt += 1
# print(fb)

# a = 0
# b = 1
# fb.append(a)
# fb.append(b)
# cnt = 2
# while cnt < 100:
#     # F(n)=F(n-1)+F(n-2)(n>=2)
#     temp = fb[cnt - 1] + fb[cnt - 2]
#     fb.append(temp)
#     cnt = cnt + 1
# print(fb)

# 斐波那契数列，首位是0，第二位是1，第三位是1....第n位是x, 第n+1位是 y, 第n+2位是 x+ y
fb = []
# 数组第一位是0
fb.append(0)
# 数组第二为是1
fb.append(1)
# 于是根据斐波那契的性质我们可以计算出第三位是第0项加第一项
c = fb[0] + fb[1]
fb.append(c)
# 第四位就是第1项加第二项
d = fb[1] + fb[2]
fb.append(d)
print(fb)

# 写成循环的形式就是
fb = []
# 数组第一位是0
fb.append(0)
# 数组第二为是1
fb.append(1)
# 计算第2项到第99项的斐波那契数列,只素以从第2项开始是以为你第1项和第0项已经计算过了
for i in range(2, 100):
    temp = fb[i - 1] + fb[i - 2]
    fb.append(temp)
print(fb)
