# -*- coding: utf-8 -*-
class Commodity(object):
    def __init__(self, id=None, price='', count=0, create_time='', shop_id='',
                 status=1, delete_time=''):
        """
        商品类
        :param id:
        :param price:地文本
        :param count:
        :param create_time:
        :param shop_id:商家id
        :param status:  0 上架 1 下架 默认下架
        delete_time
        """
        self.id = id
        self.price = price
        self.count = count
        self.create_time = create_time
        self.shop_id = shop_id
        self.status = status
        self.delete_time = delete_time
