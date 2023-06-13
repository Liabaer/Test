# -*- coding: utf-8 -*-
# 数据清洗 ：对一些没有用的数据进行处理的过程，比如很多数据存在数据缺失，数据格式错误，错误数据或重复数据的情况
# 为了使数据分析更加准确，就需要对这些没用的数据进行处理
import pandas as pd
# 使用dropna()
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

# 可以通过isnull()判断单元格是否为空 返回bool值


# df = pd.read_csv('property-data.csv', na_values=['missing_values'])
#
# print(df['NUM_BEDROOMS'])
# print(df['NUM_BEDROOMS'].isnull())
# 还可以指定空数据类型  df = pd.read_csv('property-data.csv',na_values=missing_values)


# df = pd.read_csv('property-data.csv')
# new_df = df.dropna()
# print(new_df.to_string())
# dropna() 方法返回一个新的 DataFrame，不会修改源数据。
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数

# 也可以移除指定列有空值的行
# df.dropna(subset=['ST_NUM'], inplace=True)
# print(df.to_string())

#  使用 fillna() 方法来替换一些空字段
# df.fillna(12345, inplace = True)
# print(df.to_string())

# 也可以指定某一列来替换数据
# df['PID'].fillna(12345, inplace = True)
# print(df.to_string())
# 使用 12345 替换 PID 为空数据


# 替换空单元格的常用方法是计算列的均值、中位数值或众数。
# Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。
# x = df['ST_NUM'].mean()          # 先计算均值
# df['ST_NUM'].fillna(x, inplace=True)   # 用均值替换空单元格
# print(df.to_string())
# # 同理可以使用中位数median()
# y = df['ST_NUM'].median()
# # 同理可以使用众数mode()
# z = df['ST_NUM'].mode()

# 使用pandas清洗格式错误数据
# 格式化日期 to_datatime()

# 第三个日期格式错误
# data = {
#   "Date": ['2020/12/01', '2020/12/02' , '20201226'],
#   "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#
# # 这里第一次没有加 format参数，报了如下的错误，根据错误提示，很好，英文没太明白是吧，翻译了一下 加了format='mixed'可以了，格式化了
# # ValueError: time data "20201226" doesn't match format "%Y/%m/%d", at position 2. You might want to try:
# #     - passing `format` if your strings have a consistent format;
# #     - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format;
# #     - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.
#
# # ValueError：时间数据 "20201226 "与格式"%Y/%m/%d "不匹配，在第2位。你可能想尝试一下：
# #     - 如果你的字符串有一个一致的格式，就传递`format`；
# #     - 如果你的字符串都是ISO8601，但不一定是完全相同的格式，则传递`format='ISO8601'；
# #     - 传递 "format='mixed'"，每个元素的格式将被单独推断出来。你可能想同时使用`dayfirst`。
# df['Date'] = pd.to_datetime(df['Date'],format='mixed')
#
# print(df.to_string())
#
# 修改错误数据  对错误的数据进行替换或移除
# person = {
#   "name": ['Google', 'Runoob' , 'Taobao'],
#   "age": [50, 40, 12345]    # 12345 年龄数据是错误的
# }
#
# df = pd.DataFrame(person)
# df.loc[2, 'age'] = 30 # 修改数据
# print(df.to_string())


# 可以设置条件语句
# person = {
#   "name": ['Google', 'Runoob' , 'Taobao'],
#   "age": [50, 40, 12345]
# }
#
# df = pd.DataFrame(person)
# 遍历index，大于120的都让他等于120
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.loc[x, "age"] = 120
# print(df.to_string())

# # 遍历index，大于120的都让他删除
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.drop(x, inplace=True)
#
# print(df.to_string())


# pandas 清洗重复的数据 duplicated() drop.duplicates() 返回的bool值，如果是重复的duplicated() 返回True
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)

print(df.duplicated())

# 删除重复数据，可以直接使用drop_duplicates() 方法。
df.drop_duplicates(inplace = True)
print(df)
