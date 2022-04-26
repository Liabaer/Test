# -*- coding: utf-8 -*-
# 1.当s是函数内的局部变量时，不能在函数外面使用，如果在外面使用的话，就是全局变量了，需要重新定义。相当于此s非彼s

# 表达值是false、None、0时，flag为flase,其他都是true

# reverse 的排序规则 reverse = true是降序 默认是false，是升序

# ss = [2, 3, 6, 9, 7, 1]
# for x in ss:
#     print(max(ss), end=',')
#     ss.remove(max(ss))
#     print(ss)
#
# # for循环内部等价于while循环，如下
# ss = [2, 3, 6, 9, 7, 1]
# i = 0
# while i < len(ss):
#     i = i + 1
#     print(max(ss), end=',')
#     ss.remove(max(ss))

# cs = {'aa': 4, "bb": 6}
# # 循环的是key,然后通过cs[key]取value
# for key in cs:
#     print(key, cs[key])
# # 直接循环key, value
# for key, value in cs.items():
#     print(key, value)
#
# a = {'a': 11, 'b': 5, 'c': 3}
# a.pop('c')
# print(a)

# 不写return或则只写return 等价于return None
# s = 0
# def fun(s, n):
#     for i in range(n):
#         s += i
#         print(s, i)
# print(fun(s,5))

# python里面等号的作用是赋值这个你肯定知道，但是其实给他的是地址，然后我们打印的时候打印的是地址上面的值
# 相当于在数组（内存）中找一个位置（地址）存放[10]这个变量
ls = [10]
print('ls当前内存地址是=', id(ls))
def run(n):
    ls.append(n) # ls是全局变量，我们执行a.append(n)，首先会找到这个位置，然后把n也一起放入到这个位置，于是这个位置的里面存放的东西就变成了[10,5]
    print('ls当前内存地址是=', id(ls))
run(5)
print(ls)

ls = 5
print('ls当前内存地址是=', id(ls))
def run1(n):
    ls = n # 用等于号，想当于定义了一个局部变量和全局变量同名，所以全局变量不会修改
    print('ls当前内存地址是=', id(ls))
run1(4)
print(ls)