# -*- coding: utf-8 -*-

# 定义私有函数，首先需要私有属性，私有属性一定是放在__init__的方法里的，然后我们在函数入参一定要加self,并且函数里面的代码一定要用到self.
class User_test_case(object):
    def __init__(self):
        self.case = {'email': 'RenaTuT0401@gmail.com', 'password': '34dfsdAf324sf2@s'}

    def test_login_case(self):
        return self.case
