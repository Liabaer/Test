# -*- coding: utf-8 -*-
# 第五步
# 执行登录流程，使用旧密码和新密码都尝试登录，判断是否修改成功
# ps(2种测试用例可以写成循环)
from study_project.test_case.user_test_case import UserTestCase
from study_project.test_api.user_test_api import UserTestApi

test_case = UserTestCase().test_login_case()
test_case1 = UserTestCase().test_login_case1()

login_case = [test_case, test_case1]
for case in login_case:
    auth = UserTestApi.user_get_auth(case)
    if auth is None:
       continue
    else:
        email_code = UserTestApi.user_get_code(auth, emailType='login_auth')
        # code = input()
        res = UserTestApi.user_login('123456', auth, opt='login')
        print('登陆成功，token为' + res.get('data').get('token'))