# -*- coding: utf-8 -*-
import json

import pandas as pd

# df = pd.read_json('sites.json')
#
# # to_string() 用于返回 DataFrame 类型的数据
# print(df.to_string())

# 也可以通过  pd.DataFrame(data)   【例如data就是json，传进去就好啦】

# JSON 对象与 Python 字典具有相同的格式，所以也可以直接将 Python 字典转化为 DataFrame 数据
#
# s = {
#     "col1":{"row1":1,"row2":2,"row3":3},
#     "col2":{"row1":"x","row2":"y","row3":"z"}
# }
#
# # 读取 JSON 转为 DataFrame
# df = pd.DataFrame(s)
# print(df)
#       col1 col2
# row1     1    x
# row2     2    y
# row3     3    z

# 从 URL 中读取 JSON 数据
# URL = 'https://static.runoob.com/download/sites.json'
# df = pd.read_json(URL)
# print(df)
# #

# 格式化完整内容
# df = pd.read_json('nested_list.json')
# print(df)
# 输出结果：
#           school_name   class                                           students
# 0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
# 1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
# 2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...


# import json
# # 先用 json 读取数据
# with open('nested_list.json','r') as f:
#     data = json.loads(f.read())

# 这时需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来  使用参数 record_path 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students
# df_nested_list = pd.json_normalize(data, record_path=['students'])
# print(df_nested_list)
#  输出 这个时候输出的结果没有包含 school name 和class的元素
#      id   name  math  physics  chemistry
# 0  A001    Tom    60       66         61
# 1  A002  James    89       76         51
# 2  A003  Jenny    79       90         78
#
# # 如果都展示出来，使用meta参数
# df_nested_list = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=['school_name','class']
# )
# print(df_nested_list)


# 整个更复杂的json  nested_mix.json
# nested_mix.json 文件转换为 DataFrame
# import json
# with open('nested_mix.json','r') as f:
#     data = json.loads(f.read())
#
# df = pd.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info','president'],
#         ['info','contacts','tel']
#     ]
# )
# print(df)
#      id   name  math  ...   class  info.president info.contacts.tel
# 0  A001    Tom    60  ...  Year 1     John Kasich         123456789
# 1  A002  James    89  ...  Year 1     John Kasich         123456789
# 2  A003  Jenny    79  ...  Year 1     John Kasich         123456789
#
# [3 rows x 8 columns]


# 读取内嵌数据中的一组数据。使用nested_deep.json ,只读取math字段
from glom import glom

df = pd.read_json('nested_deep.json')

data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
# 0    60
# 1    89
# 2    79
# Name: students, dtype: int64
