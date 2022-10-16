# -*- coding: utf-8 -*-
class OrderItem(object):
    def __init__(self, id=None, order_id=None, item_id=None, item_count=0, item_price=0, create_time=''):
        """
        用户购买商品类
        :param id:
        :param order_id:
        :param item_id:
        :param item_count:
        :param item_price:当前的item价格
        :param create_time:
        """
        self.id = id
        self.order_id = order_id
        self.item_id = item_id
        self.item_count = item_count
        self.item_price = item_price
        self.create_time = create_time
