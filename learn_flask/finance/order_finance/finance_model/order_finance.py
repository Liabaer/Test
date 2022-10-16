# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class OrderFinance(object):
    def __init__(self, id=None, amount=0.00, status=0, courier_id=None, user_id=None, create_time=Job.get_time()):
        """
        订单类
        :param id:
        :param amount:
        :param status:    0 下单 1 已接单 2完成
        :param courier_id:
        :param user_id:
        :param create_time:
        """
        self.id = id
        self.amount = amount
        self.status = status
        self.courier_id = courier_id
        self.user_id = user_id
        self.create_time = create_time
