# -*- coding: utf-8 -*-

# 定义私有函数，首先需要私有属性，私有属性一定是放在__init__的方法里的，然后我们在函数入参一定要加self,并且函数里面的代码一定要用到self.
class UserTestCase(object):
    def __init__(self):
        self.case = {'email': 'Rena401@gmail.com', 'password': '34dfsdAf324sf2@s'}
        self.case1 = {'email': 'Rena0401@gmail.com', 'password': '141242Tt@'}
        self.updatepwd = {'originPwd': '34dfsdAf324sf2@s', 'newPwd': '141242Tt@'}
        self.email = {'email': '06689@qq.com'}
        self.case2 = {'email': '689@qq.com', 'password': '141242Tt@'}

    def test_login_case(self):
        return self.case

    def test_login_case1(self):
        return self.case1

    def test_login_case2(self):
        return self.case2

    def test_update_pwd(self):
        return self.updatepwd

    def test_update_eml(self):
        return self.email
