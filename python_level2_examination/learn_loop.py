# -*- coding: utf-8 -*-
# 循环中多种写法以及注意事项

# case 1 利用in
# a = [1, 2, 3]
# for x in a:
#     print(x, end=' ')
# print()
#
# case 2  使用enumerate函数可以将下标和对应的值一起返回
# for index, x in enumerate(a):
#     print("下标：{} 值为 {}".format(index, x))

# case3 在case1的基础上我们自定义下标
# a = [1, 2, 3]
# index = 0
# for x in a:
#     print("下标：{} 值为 {}".format(index, x))
#     index = index + 1

# # case 4 利用range生成下标
# a = [1, 2, 3]
# for index in range(0, len(a)):
#     print("下标：{} 值为 {}".format(index, a[index]))

# # 倒序输出 利用range反向输出
# print("倒叙")
# a = [1, 2, 3]
# for index in range(len(a) - 1, -1, -1):
#     print("下标：{} 值为 {}".format(index, a[index]))
#
# # 倒序输出利用reversed
# for x in reversed(a):
#     print(x, end=' ')
# print()
#
# while循环
# a = [1, 2, 3]
# index = 0
# while index < len(a):
#     print("下标：{} 值为 {}".format(index, a[index]))
#     index = index + 1

# while循环 倒序
# a = [1, 2, 3]
# index = len(a) - 1
# while index >= 0:
#     print("下标：{} 值为 {}".format(index, a[index]))
#     index = index - 1
#
# # 在循环中对数组进行append不会有问题  for while循环都没问题
# a = [1, 2, 3]
# for x in a:
#     if x == 1:
#         a.append(4)
#     print(x, end=' ')
# print()
#
# 假设题目的意思是如果数组中存在2，则再第0位插入5的元素，并且遍历元素
# 上面的代码就是错误的做法
# 正确的做法应该是先循环判断有没有2，如果存在2就break,然后设置一个flag,在循环外面插入5

# 在循环中对数组进行insert,如果当前的insert的位置在当前循环的下标之前就有问题，在当前循环的下标之后就没问题 (while循环一样会根据情况有问题）
# a = [1, 2, 3, 4, 5]
# flag = True  # 控制只插入一次
# for x in a:
#     if x == 2 and flag:
#         flag = False
#         a.insert(0, 5)
# # insert之后数组从第0位之后，整体向右偏移一位变成[5, 1, 2, 3, 4, 5], 这个时候访问的下标是a[1],下次访问的是a[2]也就是2,老的a[1]和新的a[2]是一个值（因为整体向右移动一位）所以有问题
# # a.insert(3, 6)  # 没问题，insert之后数组从第3位之后整体向右偏移一位变成[5, 1, 2, 6, 4, 5],这个时候访问的下标是a[1],下次访问a[2]还是正常的值，因为从a[3]后才开始偏移，所以没问题
#     print(a[x], end=' ')
# print(a)

# 在循环中对数组进行remove操作，如果remove的元素所在的下标在当前循环的下标之前，那会有问题。如果在当前循环的下标之后就没问题 (while循环一样会根据情况有问题）
# a = [1, 2, 3, 4, 5]
# flag = True  # 控制只remove一次
# for x in a:
#     if x == 2 and flag:
#         a.remove(1)  # 有问题，remove后，数组的整体向左边偏移1位变成了[2,3,4,5]但是当前循环的下标还是在a[1]这个位置，下次循环就是a[2]的位置也就是4，所以不会打印3这个元素
#         # a.remove(3) # 没问题，remove后，数组元素3之后的整体向左偏移了一位[1,2,4,5],但是当前循环的下标是a[1]，下次循环a[2]也就是4，所以没问题
#         flag = False
#     print(x, end=' ')
# print()
#
# # 循环表达式

# # 假设我们需要通过循环提取数组元素放入新的数组
# a = [1, 2, 3, 4, 5, 6]
# b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x)
# print(b)
#
# # 使用循环表达式简写
# a = [1, 2, 3, 4, 5, 6]
# # # 这里首先先写循环条件
# # # for x in a
# # # 然后继续写if条件
# # # for x in a if x % 2 == 0
# # # 然后我们要的是数组给他打上中括号表示生成的是数组
# # # [for x in a if x % 2 == 0]
# # # 最后我们要把每次循环得到的满足条件的x放在最前面
# # # [x for x in a if x % 2 == 0] 表示循环a，如果元素x满足条件的话就放入到新数组中（for x in a if x % 2 == 0）这个可以看成是个函数，然后return了x,然后把x自动放入数组
# # b = [x for x in a if x % 2 == 0]
# # print(b)
# #
# # # 还可以对x进行操作运算操作
# b = [str(x) + "我是偶数" for x in a if x % 2 == 0]
# print(b)

# 集合也可以
a = [1, 2, 2, 3, 3, 4, 4]
# 将中括号改成大括号
b = {x for x in a if x % 2 == 0}
# 去重了
print(b)

# 字典写法特殊一点
a = {'a': [1, 2], 'b': [2, 3], 'c': [2, 3, 4]}
# 将中括号改成大括号,然后之前的x我们需要替换成key:value的形式
b = {key + '我是新的key': a[key] for key in a if len(a[key]) < 3}
print(b)