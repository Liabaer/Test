# -*- coding: utf-8 -*-
class Shop(object):
    def __init__(self, id=None, name='', password='', status=0, review_score_avg=0.00, review_count=0):
        # 商家
        # 1. id
        # 2. name
        # 3. password
        # 4. status 0 上架 1下架
        # 5. review_score_avg 有效评分
        # 6. review_count 有效总数
        self.id = id
        self.name = name
        self.password = password
        self.status = status
        self.review_score_avg = review_score_avg
        self.review_count = review_count
