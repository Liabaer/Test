# -*- coding: utf-8 -*-
# a = [1, 2, 3]
# # 移除某个元素，如果元素不存在会报错
# a.remove(2)
# # insert(i, x) 在第i位插入新元素x
# a.insert(1, 5)
# print(a)


# # 复制数据
# a1 = a.copy()
# print(a1)
#
# # 清空数组
# a = [1, 2, 3]
# a.clear()
# print(a)

# # # 将数组倒序
# a = [1, 2, 3]
# # 注意不需要重新赋值给a
# a.reverse()
# print(a)
#
# a = [1, 1, 1, 4, 5]
# # 统计数组中某个元素的个数
# print(a.count(1))
# print(a.count(2))
# #
#
# # type函数：输出变量的类型
# print(type('a'))
# print(type({'a', 'b'}))

# # zip将数组a和数组b合并转换为元祖
# a = [1, 2, 3]
# b = [3, 4, 5]
# c = list(zip(a, b))
# print(c)

# # set 初始化集合
# # 定义一个空集合
# a = set()
# print(a)
# # 直接定义一个空集合，并且赋值，这里需要注意，这里的赋值后，他会去重，而且顺序会打乱
# a = set("habcdaa")
# print(a)
#
#
# # 求出数组里的最大值和最小值
# a = [1, 2, 3]
# print(max(a))
# print(min(a))
#
# # 求出字典里最大的键 key
# a = {1:'a', 2:'b', 3:'c'}
# print(max(a))
# print(min(a))
# #
# # # # 字典
# a = {1:'a', 2:'b', 3:'c'}
# # # 输出所有的key, 会输出dict_keys([1,2,3])这个，因为他属于dict_keys类型
# # print(a.keys())
# # # 删除key，如果key不存在会报错 KeyError
# # a.pop(1)
# # print(a)
# # # a.pop(4)  # 报错
# # # # 这种容错的写法就不会报错，如果4不存在，则去删除为5的key,5不存在也不会报错
# # a.pop(4, 5)
# # print(a)
# # # 上面的写法类似与
# # # 不存在key，会返回None
# print(a.get(4))
# # 不存在key，返回默认值第二个参数
# print(a.get(4, 100))