# -*- coding: utf-8 -*-
from learn_project.my_project.test_case.user_test_case import UserTestCase
from learn_project.my_project.test_api.user_test_api import UserTestApi

test_case2 = UserTestCase().test_login_case2()
test_case1 = UserTestCase().test_login_case1()

login_case = [test_case2, test_case1]
for case in login_case:
    auth = UserTestApi.user_get_auth(case)
    if auth is None:
        continue
    else:
        email_code = UserTestApi.user_get_code(auth, emailType='login_auth')
        # code = input()
        res = UserTestApi.user_login('123456', auth, opt='login')
        print('登陆成功，token为' + res.get('data').get('token'))
