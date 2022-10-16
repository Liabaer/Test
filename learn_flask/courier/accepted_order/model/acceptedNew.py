# -*- coding: utf-8 -*-
class OrderNewLog(object):
    def __init__(self, id=None, status=0, courier_id=None, user_id=None, send_time='', admin_id=None, timeout_time='',
                 accepted_time='', un_accepted_time=''):
        """

        订单类
        :param id:
        :param status:    0下单 1 已接单 2 配送中 3 配送完成
        :param courier_id:
        :param user_id:
        admin_id 操作员id
        timeout_time 超时时间
        accepted_time 接单时间
        un_accepted_time 未抢到时间
        """
        self.id = id
        self.status = status
        self.courier_id = courier_id
        self.user_id = user_id
        self.send_time = send_time
        self.admin_id = admin_id
        self.timeout_time = timeout_time
        self.accepted_time = accepted_time
        self.un_accepted_time = un_accepted_time
