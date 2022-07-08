# -*- coding: utf-8 -*-
class Coupon(object):
    def __int__(self,id=None,coupon_price='',coupon_discount='',type='',create_time=''):
        """
        优惠券
        :param id:
        :param coupon_price:直接优惠金额
        :param coupon_discount:优惠折扣 小数0.005之类
        :param type:0 等于直接优惠 1等于优惠折扣
        :param create_time:
        :return:
        """
        self.id = id
        self.coupon_price = coupon_price
        self.coupon_discount = coupon_discount
        self.type=type
        self.create_time = create_time