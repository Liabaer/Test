# -*- coding: utf-8 -*-
from study_project.test_case.user_test_case import test_login_case
from study_project.test_api.user_test_api import user_get_auth,user_get_code,user_login

# 获取测试用例
test_case = test_login_case()

auth = user_get_auth(test_case)
print(auth)

#获取验证码
user_get_code(auth)
#输入验证码
email_code = input()

# 登陆
res = user_login(email_code,auth)
print(res)