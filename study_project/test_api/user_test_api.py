# -*- coding: utf-8 -*-
import requests

from  study_project.test_case.user_test_case import test_login_case
from study_project.test_setting.setting import bese_url, hd

class getUrl(object):
    def user_get_auth(self, data=""):
        """
        登陆获取auth
        :return:
        """
        res = requests.post(bese_url + '/api/user/pre-login', headers=hd, json=data)
        auth = res.json().get('data').get('authId')
        return auth

    def user_get_code(self, auth):
        """
        获取验证码
        :return:
        """
        eml = requests.post(bese_url + '/api/user/auth-email',headers=hd,json={'authId': auth, 'emailType': 'login_auth'})



    def user_login(self, email_code='', auth=''):
        """
        登陆
        :param email_code:
        :param auth:
        :return:
        """
        lgn = requests.post(bese_url + '/api/user/auth',
                            headers=hd,
                            json={'authId': auth, 'authType': 'email_auth', 'authText': email_code, 'operator': 'login'})
        return lgn.json()