# -*- coding: utf-8 -*-
from study_project.test_case.user_test_case import UserTestCase
from study_project.test_api.user_test_api import UserTestApi

# 获取测试用例
test_case = UserTestCase().test_login_case()

auth = UserTestApi.user_get_auth(test_case)
print(auth)

#获取验证码
code = UserTestApi.user_get_code(auth)
#输入验证码
email_code = input()

# 登陆
res = UserTestApi.user_login(email_code,auth)
print(res)