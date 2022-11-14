# -*- coding: utf-8 -*-

# Mock 步骤如下：
# 导入 unittest 框架中的 mock
# 找到要替换的对象A，可以是一个类、函数或者类实例
# 实例化mock对象，设置mock对象的行为，比如调用的时候返回的值，被访问成员的时候返回什么值等。
# 使用mock对象替换对象A
# 调用并断言


# import unittest
# from unittest import mock

#
# class LoginClass():
#     def login_test(self, url, data):
#         pass
#
#
# class TestRegister(unittest.TestCase):
#     def test01(self):
#         login01 = LoginClass()
#         # 实例化mock对象，指定返回值，替换原有对象
#         login01.login_test = mock.Mock(
#             return_value={"code": 200, "msg": "登陆成功"})
#         url = "http://127.0.0.1:8000/login"
#         data = {"username": "aa", "pwd": "123456"}
#         res = login01.login_test(url,data)
#         self.assertEqual(res["code"], 200)
#
#
# if __name__ == "__main__":
#     unittest.main()




# import unittest
# from unittest import mock
# import demo
#
#
# # 通过mock，单元测试分别测试正常返回和异常返回情况
#
# class TestReq(unittest.TestCase):
#     def test_request_01(self):
#         # 实例化mock对象，指定返回值，替换原有对象
#         demo.send_request = mock.Mock(return_value='200')
#         print(demo.send_request())
#         self.assertEqual(demo.visit_baidu(),'200')
#
#
#     def test_request_02(self):
#         demo.send_request = mock.Mock(return_value='400')
#         print(demo.send_request())
#         self.assertEqual(demo.visit_baidu(),'400')
#
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)



# 高级用法 mock库提供了patch函数来简化mock对象对原对象的替换，
# 该函数会返回一个mock内部的类实例，它可以控制mock的范围，可以作为装饰器或者上下文管理器使用。

import unittest
from unittest import mock
import demo


# 通过mock，单元测试分别测试正常返回和异常返回情况

class TestReq(unittest.TestCase):
    #在测试的参数里对该mock对象设置一个参数
    @mock.patch("demo.send_request")
    def test_request_01(self, mock_request):
        # 指定一个返回值
        mock_request.return_value = '200'
        self.assertEqual(demo.visit_baidu(), '200')

    @mock.patch("demo.send_request")
    def test_request_02(self,mock_request):
        # 指定一个返回值
        mock_request.return_value = '400'
        self.assertEqual(demo.visit_baidu(), '400')



if __name__ == '__main__':
    unittest.main(verbosity=2)