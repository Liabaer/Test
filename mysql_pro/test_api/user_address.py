# -*- coding: utf-8 -*-
class UserAddress(object):
    def __init__(self, id=None, address_text='', address_location='', create_time='', user_id=None,
                 status=0):
        """
        用户地址类
        :param id:
        :param address_text:地址文本
        :param address_location:地址经纬度
        :param create_time:
        :param user_id:用户的id
        :param status: 0 正常 1 删除
        """
        self.id = id
        self.address_text = address_text
        self.address_location = address_location
        self.create_time = create_time
        self.user_id = user_id
        self.status = status
