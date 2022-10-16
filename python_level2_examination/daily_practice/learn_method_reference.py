# -*- coding: utf-8 -*-
# 函数中变量的传递


# a = 1
# def update_int(temp):
#     temp = 2
#     print(temp)
# update_int(a)
# # 不会修改结果，因为此时传入的a,相当于a 指向1， temp=a,也指向1的地址，所以temp=2的时候temp指向了2，a不会变
# print(a)

# a = [1, 2, 3]
# def update_list(temp):
#     temp = [2, 3, 4]
#     print(temp)
# update_list(a) # 和上面同理
# print(a)
#
# a = [1, 2, 3]
# def update_list2(temp):
#     temp[0] = 3
#     # 除了上述这种修改，类似append,insert都会修改地址中的元素
#     temp.append(4)
#     temp.insert(2, 100)
#     print(temp)
# update_list2(a) # 此时a和temp都指向的是[1,2,3]地址，temp修改[1,2,3]的地址为[3,2,3]，a的结果
# print(a)
# #
#
# 比较特殊的情况
# def update_list3(temp=[]):
#     temp.append(1)
#     print(temp)
# # temp会在内存中一直追加1，从[]修改为[1],[1,1]...
# 调用的函数没有传值时才会修改函数定义的值，传了参数就不会改
# update_list3()
# update_list3()
# update_list3()

# def func(x=[], y=[6, 7]):
#     x.append(8)
#     y.append(8)
#     return (x+ y)
#
# a,b=[1,2],[3,4]
# # t=func(x=a),y没有传值，所以让y的默认值从[]变成了[6,7,8]，x不变还是[]
# t = func(x=a)
# print(t)
# # 第二个t = func(y=b), x没有传值 这个时候让x的默认值从[]变成了[8] y不变，是[6,7,8]
# t = func(y=b)
# print(t)
# print(func(), end=";")
