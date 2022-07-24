# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class SettleAccount(object):
    def __init__(self, id=None, amount=0.00, status=0, courier_id=None, order_id=None, create_time=Job.get_time()):
        """
        订单结算类
        :param id:
        :param amount:
        :param status:    0 待结算 1 已结算
        :param courier_id:
        :param order_id:
        :param create_time:
        """
        self.id = id
        self.amount = amount
        self.status = status
        self.courier_id = courier_id
        self.order_id = order_id
        self.create_time = create_time
