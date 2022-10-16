# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class StudentConsumer(object):
    def __init__(self, id=None, amount=0, type=0, create_time=Job.get_time()):
        """
        学生消费类
        :param id:
        :param amount:余额
        :param create_time:
        :param type:0 消费 1充值
        """
        self.id = id
        self.amount = amount
        self.type = type
        self.create_time = create_time
