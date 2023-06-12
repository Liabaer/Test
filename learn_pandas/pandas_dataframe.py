# -*- coding: utf-8 -*-
# DataFrame 是pandas的一种数据结构 是一个二维的数组结构，类似二维数组
# DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
# DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
#
# 参数
# pandas.DataFrame(data="一组数据（ndarray,series,map,lists,dict等类型）", index= "索引值or行tag", columns="列标签默认为RangeIndex（0,1,2...,n）", dtype="数据类型", copy="copy数据，默认是False")


import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
# 本来是酱紫的，但是执行发现报错：could not convert string to float: 'Google'

# 然后我解决了一下，我让他都是str再单独把age转成数字类型
# df = pd.DataFrame(data,columns=['Site','Age'],dtype=str)
# # 使用pd.to_numeric()方法将’Site’列转换为数字值。errors ='coerce'参数告诉pandas将任何非数字值替换为NaN。
# df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# print(df)
# 输出
#      Site  Age
# 0  Google   10
# 1  Runoob   12
# 2    Wiki   13

# ps：插播一条：NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
# 创建一个 ndarray 只需调用 NumPy 的 array 函数即可：
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# object 数组或嵌套的数列
# dtype	数组元素的数据类型，可选
# copy	对象是否需要复制，可选
# order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
# subok	默认返回一个与基类类型一致的数组
# ndmin	指定生成数组的最小维度
# 多于一个维度
# import numpy as np
# a = np.array([[1,  2],  [3,  4]])
# print (a)
# dtype 参数
# import numpy as np
# a = np.array([1,  2,  3], dtype = complex)
# print(a)


# 然后使用 ndarrays 创建，ndarray 的长度必须相同，
# 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。

# data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
#
# df = pd.DataFrame(data)
# print(df)
# #      Site  Age
# 0  Google   10
# 1  Runoob   12
# 2    Wiki   13




# 使用字典创建 字典（key/value），其中字典的 key 为列名:
#
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
#
# df = pd.DataFrame(data)
#
# print(df)
#    a   b     c
# 0  1   2   NaN      没有对应的部分数据为 NaN。
# 1  5  10  20.0

# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# # 数据载入到 DataFrame 对象
# df = pd.DataFrame(data)
# print(df)
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45
# 返回第一行
# print(df.loc[0])
# calories    420
# duration     50
# Name: 0, dtype: int64   name就是行的index

# 返回第二行
# print(df.loc[1])
# calories    380
# duration     40
# Name: 1, dtype: int64
#  ps ：返回结果其实就是一个 Pandas Series 数据。
#


# 也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引
# print(df.loc[[0, 1]])
#    calories  duration
# 0       420        50
# 1       380        40
# 返回结果其实就是一个 Pandas DataFrame 数据




data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df)
# 指定index
#       calories  duration
# day1       420        50
# day2       380        40
# day3       390        45

# 同样可以指定返回某一index的值
# print(df.loc["day2"])
# calories    380
# duration     40
# Name: day2, dtype: int64
