# -*- coding: utf-8 -*-
class Admin(object):
    def __init__(self,id=None,name='',phone_number='',password='',role=0):
        """
        管理员类
        :param id:
        :param name:
        :param phone_number:
        :param password:
        :param role: 0 无权限 1admin权限 2 审核员权限
        """
        self.id = id
        self.name = name
        self.phone_number=phone_number
        self.password = password
        self.role = role