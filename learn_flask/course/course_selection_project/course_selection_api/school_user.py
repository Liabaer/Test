# -*- coding: utf-8 -*-
class SchoolUser(object):
    def __init__(self, id=None, name='', type=0, create_time='', password=''):
        """
        学校用户类
        :param id:学号
        :param name:姓名
        :param type: 0学生，1老师
        :param create_time:创建时间
        :param password:密码
        """
        self.id = id
        self.name = name
        self.type = type
        self.create_time = create_time
        self.password = password
