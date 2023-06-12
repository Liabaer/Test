# -*- coding: utf-8 -*-
import pandas as pd
#
df = pd.read_csv('nba.csv')

# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替
# print(df.to_string())
# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。
# print(df.head(10))
# tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
# print(df.tail())
# info() 方法返回表格的一些基本信息
print(df.info)
# <class 'pandas.core.frame.DataFrame'>    类型
# RangeIndex: 458 entries, 0 to 457          # 行数，458 行，第一行编号为 0
# Data columns (total 9 columns):            # 列数，9列
#  #   Column    Non-Null Count  Dtype       # 各列的数据类型
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   373 non-null    object         # non-null，意思为非空的数据
#  8   Salary    446 non-null    float64
# dtypes: float64(4), object(5)                 # 类型合计
# non-null 为非空数据，我们可以看到上面的信息中，总共 458 行，College 字段的空值最多



# 使用 to_csv() 方法将 DataFrame 存储为 csv 文件
# 三个字段 name, site, age
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
#
# # 字典
# dict = {'name': nme, 'site': st, 'age': ag}
#
# df = pd.DataFrame(dict)
#
# # 保存 dataframe
# df.to_csv('site.csv')
