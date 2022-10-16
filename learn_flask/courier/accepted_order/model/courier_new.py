# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class CourierNew(object):
    def __init__(self, id=None, name='', password='', create_time=Job.get_time()):
        """
        管理员类
        :param id:
        :param name:
        :param amount:
        :param password:
        """
        self.id = id
        self.name = name
        self.password = password
        self.create_time = create_time
