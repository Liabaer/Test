# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class UserNew(object):
    def __init__(self, id=None, name='', password='', type=0, create_time=Job.get_time()):
        """
        管理员类
        :param id:
        :param name:
        :param type: 0 顾客 1后台管理员
        :param password:
        """
        self.id = id
        self.name = name
        self.password = password
        self.type = type
        self.create_time = create_time
