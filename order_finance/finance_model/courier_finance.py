# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class CourierFinance(object):
    def __init__(self, id=None, name='', password='', amount=0.00, create_time=Job.get_time()):
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
        self.amount = amount
        self.create_time = create_time