# -*- coding: utf-8 -*-
class UserCoupon(object):
    def __init__(self, id=None, coupon_id=None, user_id=None, status=0, create_time='', user_time=''):
        """
        3. 用户优惠券类
        :param id:
        :param coupon_id:优惠券id
        :param user_id: 用户id
        :param status: 0未使用 1使用
        :param create_time:创建时间
        :param user_time:使用时间
        """
        self.id = id
        self.coupon_id = coupon_id
        self.user_id = user_id
        self.status = status
        self.create_time = create_time
        self.user_time = user_time
