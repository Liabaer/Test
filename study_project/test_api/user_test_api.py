# -*- coding: utf-8 -*-
import requests

from study_project.test_case.user_test_case import UserTestCase
from study_project.test_setting.setting import Setting

class UserTestApi(object):
    base_url = Setting.set_url()
    hd = Setting.set_hd()

    @staticmethod
    def user_get_auth(data=''):
        """
        登陆获取auth
        :return:
        """
        # 这里的data，由于类User_test_case()的test_login_case()函数的是私有的，所以相当于要new一个对象来调用
        # data = UserTestCase().test_login_case()  这里注释，是因为函数直接使用动态传入，减少耦合
        res = requests.post(UserTestApi.base_url + '/api/user/pre-login', headers=UserTestApi.hd, json=data)
        auth = res.json().get('data').get('authId')
        return auth

    @staticmethod
    def user_get_code(auth):
        """
        获取验证码
        :return:
        """
        eml = requests.post(UserTestApi.base_url + '/api/user/auth-email', headers=UserTestApi.hd, json={'authId': auth, 'emailType': 'login_auth'})


    @staticmethod
    def user_login(email_code='', auth=''):
        """
        登陆
        :param email_code:
        :param auth:
        :return:
        """
        lgn = requests.post(UserTestApi.base_url + '/api/user/auth',
                            headers=UserTestApi.hd,
                            json={'authId': auth, 'authType': 'email_auth', 'authText': email_code, 'operator': 'login'})
        return lgn.json()

