# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class Customer(object):
    def __init__(self,id=None,amount=0,name='',password='',create_time=Job.get_time()):
        """
        顾客
        :param id:
        :param amount:
        :param name:
        :param password:
        :param create_time:
        """
        self.id = id
        self.amount = amount
        self.name = name
        self.password = password
        self.create_time = create_time