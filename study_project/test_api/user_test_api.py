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
        if 'data' in res.json() and res.json().get('data') != None:
            auth = res.json().get('data').get('authId')
            return auth
        else:
            print('登陆错误原因是：'+ res.json().get('message'))
            return None
        # if res.status_code == 200:
        #     print(res.text)
        #     auth = res.json().get('data').get('authId')
        #     return auth
        # else:
        #     print(res.content)
        #     return None


    @staticmethod
    def user_get_code(auth, emailType=''):
        """
        获取验证码
        :return:
        """
        eml = requests.post(UserTestApi.base_url + '/api/user/auth-email',
                            headers=UserTestApi.hd, json={'authId': auth, 'emailType': emailType})


    @staticmethod
    def user_login(email_code='', auth='', opt=''):
        """
        登陆
        :param email_code:
        :param auth: 验证码
        :param opt: 操作
        :return:
        """
        lgn = requests.post(UserTestApi.base_url + '/api/user/auth',
                            headers=UserTestApi.hd,
                            json={'authId': auth, 'authType': 'email_auth', 'authText': email_code, 'operator': opt})
        return lgn.json()

    @staticmethod
    def update_passwod(originPwd='', newPwd=''):
        """
        修改密码
        :param token: 获取登陆的token
        :param originPwd: 旧密码
        :param newPwd: 新密码
        :return: 返回修改后authId
        """

        update_pwd = requests.post(UserTestApi.base_url+'/api/user/update-password',
                                   headers=UserTestApi.hd,
                                   json={'originPassword':originPwd, 'newPassword':newPwd})
        return update_pwd.json()
