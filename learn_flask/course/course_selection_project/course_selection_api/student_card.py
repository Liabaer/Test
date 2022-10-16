# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class StudentCard(object):
    def __init__(self, id=None, amount=0, name='', create_time=Job.get_time()):
        """
        学生卡类
        :param id:
        :param name:分类名（如计算机）
        :param amount:余额
        :param create_time:
        :param status:0 正常 1 删除
        """
        self.id = id
        self.name = name
        self.amount = amount
        self.create_time = create_time
