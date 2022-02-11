# -*- coding: utf-8 -*-
# 对于非负整数X而言，X的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果X = 1231，那么其数组形式为[1,2,3,1]。
#
# 给定非负整数 X 的数组形式A，返回整数X+K的数组形式。
A = [1, 2, 0, 0]
K = 34
res = []
# 这是使用函数的方法
# map(str,A)是让A里面的每个元素变成str元素 ,list()将里面的都变成数组
A = list(map(str, A))
# print(A)
A = int("".join(A)) + K
# print(A)
A = str(A)
j = 0
while j < len(A):
    res.append(int(A[j]))
    j = j + 1
print(res)




# 这是转成int然后用加法方式计算结果
# s = ''
# s1 = ''
# res = []
# i = 0
# while i < len(A):
#     s = s + str(A[i])
#     i = i + 1
# s1 = int(s) + K
# print(s1)
# s1 = str(s1)
# j = 0
# while j < len(s1):
#     res.append(int(s1[j]))
#     j = j + 1
# print(res)