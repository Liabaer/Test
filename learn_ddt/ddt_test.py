# -*- coding: utf-8 -*-
# 导入ddt下的所有内容
import unittest

from ddt import *


# （一）传递基础数据类型

# 在测试类必须先申明使用ddt
# @ddt
# class imoocTest(unittest.TestCase):
#
#     # int
#     @data(1, 2, 3, 4)
#     def test_int(self, i):
#         print("test_int:", i)
#
#     # str
#     @data("1", "2", "3")
#     def test_str(self, str):
#         print("test_str:", str)


# （二）传递一个复杂的数据结构


# @unpack：当传递的是复杂的数据结构时使用。比如使用元组或者列表，添加 @unpack 之后，
# ddt 会自动把元组或者列表对应到多个参数上。字典也可以这样处理
#
#
# @ddt
# class inoocTest(unittest.TestCase):
#     turples = ((1, 2, 3), (1, 2, 3))
#     lists = [[1, 3, 3], [1, 2, 3]]
#
#     # 当没有加unpack时，test_case方法的参数只能填一个；如元组的例子
#     # 元组
#     @data((1, 2, 3), (1, 2, 3))
#     def test_tuple(self, n):
#         print("test_tuple", n)
#
#     # 当你加了unpack时，传递的数据量需要一致；
#     # 如列表例子中，每个列表我都固定传了三个数据，当你多传或少传时会报错，而test_case方法的参数也要写三个，需要匹配上
#     # 列表
#     @data([1, 3, 3], [1, 2, 3])
#     @unpack
#     def test_list(self, n1, n2, n3):
#         print("test_list:", n1, n2, n3)
#
#     # 元组2  当传的数据是通过变量的方式，如元组2、列表2，变量前需要加上*
#     @data(*turples)
#     def test_tuples(self, n):
#         print("test_tuple:", n)
#
#     # 列表2
#     @data(*lists)
#     @unpack
#     def test_lists(self, n1, n2, n3):
#         print("test_list", n1, n2, n3)
#
#     # 当传的数据是字典类型时，要注意每个字典的key都要一致，test_case的参数的命名也要一致；
#     # 如字典的例子，两个字典的key都是value1和value2，而方法的参数也是
#     # 字典
#     @data({'value1': 1, 'value2': 2}, {'value1': 1, 'value2': 2})
#     @unpack
#     def test_dict(self, value1, value2):
#         print("test_dict", value1, value2)






# （三）DDT基础使用：传递json文件
#
# @ddt
# class imoocTest(unittest.TestCase):
#     相对路径
#     @file_data('config/testddt.json')
#     def test_json(self, data):
#         print(data)


# （三）DDT基础使用 ：传递Yaml文件

@ddt
class imoocTest(unittest.TestCase):

    @file_data("config/testddt.yaml")
    def test_yaml(self,data):
        print('yaml', data)

