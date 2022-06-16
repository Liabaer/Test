# -*- coding: utf-8 -*-
from study_project.test_case.user_test_case import UserTestCase
from study_project.test_api.user_test_api import UserTestApi

# 获取测试用例
test_case = UserTestCase().test_login_case()

auth = UserTestApi.user_get_auth(test_case)
print(auth)

# 获取验证码
code = UserTestApi.user_get_code(auth, 'login_auth')
# 输入验证码
email_code = input()

# 登陆
res = UserTestApi.user_login(email_code, auth,'login')
print(res)
token=res.get('data').get('token')
# 修改密码
updatepwd_case = UserTestCase().test_update_pwd()
updatepwd = UserTestApi.update_passwod(token=token,
                                       originPwd=updatepwd_case.get('originPwd'),
                                       newPwd=updatepwd_case.get('newPwd'))
print(updatepwd)
newauth = updatepwd.json().get('data').get('authId')
# 发送邮件
code_pwd = UserTestApi.user_get_code(newauth, 'reset_password_auth')

email_code = input()
res = UserTestApi.user_login(email_code, auth,'update_password')
print(res)