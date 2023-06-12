# -*- coding: utf-8 -*-
# Pandas 数据结构 - Series:类似表格中的一个列，一位数组，可以保存任何数据类型
# series 由索引（index）和 列组成
import pandas as pd

# pandas.Series(data="一组数据（ndarray类型）",index="数据索引标签，如果不指定，默认从0开始",dtype="数据类型，默认会自己判断",name="设置名称",copy="拷贝数据，默认为false")
# a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar)
# 输出结果：   如果没由指定索引，就从0开始，可以根据索引值读取数据
# 索引  数据
# 0    1
# 1    2
# 2    3
# dtype: int64  数据类型
# print(myvar[1])  输出 2


# a = ["Google", "Runboob", "Wiki"]
# myvar = pd.Series(a,index=["x", "y", "z"])
# print(myvar["y"])
# # 指定索引
# x     Google
# y    Runboob
# z       Wiki
# dtype: object


#我们也可以使用 key/value 对象，类似字典来创建 Series：
#
# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
#
# myvar = pd.Series(sites)
#
# print(myvar)
# 字典的 key 变成了索引值
# 1    Google
# 2    Runoob
# 3      Wiki
# dtype: object

# 如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可 还有 设置 Series 名称参数

# import pandas as pd
#
# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
#
# myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST" )
#
# print(myvar)

# 1    Google
# 2    Runoob
# Name: RUNOOB-Series-TEST, dtype: object
