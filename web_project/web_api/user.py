# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class User(object):
    def __init__(self, id=None, phone_number='', password='', create_time=Job.get_time()):
        """
        用户类
        :param id:
        :param password:
        :param phone_number:
        :param create_time:
        """
        self.id = id
        self.password = password
        self.phone_number = phone_number
        self.create_time = create_time
