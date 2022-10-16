# -*- coding: utf-8 -*-
# nums = [2, 2, 1]
# a = {}
# for i in range(0, len(nums)):
#     if nums[i] not in a:
#         a[nums[i]] = 1
#     else:
#         a[nums[i]] = a[nums[i]] + 1
# print(a)
# for b in a:
#     if a[b] == 1:
#         print(b)

# a = ["h","e","l","l","o"]
# # # b = []
# # # for i in reversed(a):
# # #     b.append(i)
# # # print(b)
# #
# print(a[::-1])

# -*- coding: utf-8 -*-

# 类
# 定义类名
# class RecentCounter(object):
#
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
# # 类似java new一个对象
# # 通过a = RecntCounter() 得到a对象，这样a对象就可以调用类的方法和变量了
# a = RecentCounter()
# print(a.add(1 ,2))
# print(a.sub(1, 2))

# 定义类名
class RecentCounter(object):
    def __init__(self):
        # 初始化方法 主要用于定义全局变量
        self.c = 10

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def add_glob(self, a, b):
        # 这个表示a + b + 一个全局变量c ，a和b是局部变量通过调用方法传入
        return a + b + self.c


# 类似java new一个对象
# 通过a = RecntCounter() 得到a对象，这样a对象就可以调用类的方法和变量了
a = RecentCounter()
print(a.add(1, 2))
print(a.sub(1, 2))
print(a.add_glob(1, 2))
