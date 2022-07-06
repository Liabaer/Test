# -*- coding: utf-8 -*-
class User(object):
    def __init__(self, id=None, name='', email='', phone_number='', password='', amount=0, create_time='', is_login=0,
                 last_login_time=''):
        """
        :param id:
        :param name: 姓名
        :param email: 邮箱
        :param phone_number: 手机号
        :param password: 密码
        :param amount: 用户充值余额
        :param create_time: 注册时间
        :param is_login: 是否登录 0 未登录 1 登录
        :param last_login_time: 最后一次登录时间
        """
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.amount = amount
        self.create_time = create_time
        self.is_login = is_login
        self.last_login_time = last_login_time
