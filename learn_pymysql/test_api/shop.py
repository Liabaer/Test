# -*- coding: utf-8 -*-
class Shop(object):
    def __init__(self, id=None, address_text='', address_location='', create_time='', name='',
                 status=1):
        """
        商家类
        :param id:
        :param address_text:地址文本
        :param address_location:地址经纬度
        :param create_time:
        :param name:商家名
        :param status: 0 营业 1 关闭
        """
        self.id = id
        self.address_text = address_text
        self.address_location = address_location
        self.create_time = create_time
        self.name = name
        self.status = status
