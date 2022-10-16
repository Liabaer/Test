# -*- coding: utf-8 -*-
from learn_project.my_project.test_case.user_test_case import UserTestCase
from learn_project.my_project.test_api.user_test_api import UserTestApi

case = UserTestCase().test_login_case1()
# 获取auth
auth = UserTestApi.user_get_auth(case)
# 先登录
code = UserTestApi.user_get_code(auth, 'login_auth')
login = UserTestApi.user_login('123456', auth, opt='login')
# 获取token
token = login.get('data').get('token')
header = UserTestApi.hd
# authorization放入header并将token赋值给authorization
header['authorization'] = token
eml = UserTestCase().test_update_eml()
# print(eml)
res = UserTestApi.update_email(eml.get('email'))
