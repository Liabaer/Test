# -*- coding: utf-8 -*-
class MySQLCourier(object):
    def __init__(self, id='', status='offine', delivery_type='delivery', courier_location='', create_time='',
                 last_online_time='', courier_email=''):
        """

        :param id: 骑手的id 格式（数据库自增）
        :param status: 骑手的在线状态 格式（offline\online)
        :param delivery_type: 骑手的类型 格式(delivery\shop_delivery)
        :param courier_location: 骑手实时位置 格式（-101.22,2.231)
        :param create_time:  骑手注册时间 （获取系统当前实时时间）
        :param last_online_time: 骑手最近一次上线时间
        :param courier_email: 邮件
        """
        self.id = id
        self.status = status
        self.delivery_type = delivery_type
        self.courier_location = courier_location
        self.create_time = create_time
        self.last_online_time = last_online_time
        self.courier_email = courier_email
