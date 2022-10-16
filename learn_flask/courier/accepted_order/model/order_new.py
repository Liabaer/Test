# -*- coding: utf-8 -*-


class OrderNew(object):
    def __init__(self, id=None, status=0, courier_id=None, user_id=None):
        """
        订单类
        :param id:
        :param status:    0下单 1 已接单 2 配送中 3 配送完成
        :param courier_id:
        :param user_id:
        """
        self.id = id
        self.status = status
        self.courier_id = courier_id
        self.user_id = user_id
