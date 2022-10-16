# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class Courier(object):
    def __init__(self, id=None, name='', status=0, create_time=Job.get_time(), phone_number='', password='', is_ready=0,
                 id_card=''):
        """
        配送员类
        :param id:
        :param name:
        :param status: 0审核中 1 审核通过 2 审核拒绝
        :param create_time:
        :param phone_number:
        :param password:
        :param is_ready:
        :param id_card:
        """
        self.id = id
        self.name = name
        self.status = status
        self.create_time = create_time
        self.phone_number = phone_number
        self.password = password
        self.is_ready = is_ready
        self.id_card = id_card
