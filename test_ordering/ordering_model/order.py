# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class Order(object):
    def __init__(self, id=None, user_id=None, status=0, amount=0.00, shop_id=None,create_time=Job.get_time()):
        # 订单
        # 1. id
        # 2. status 0 下单 1 完成
        # 3. create_time
        # 4. user_id
        # 5. amount
        # 6. shop_id
        self.id = id
        self.user_id = user_id
        self.status = status
        self.amount = amount
        self.shop_id = shop_id
        self.create_time = create_time