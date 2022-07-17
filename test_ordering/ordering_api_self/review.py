# -*- coding: utf-8 -*-
class Review(object):
    def __init__(self, id=None, shop_id=None, user_id=None, content='', update_content='', create_time='', status=0,
                 update_time='', shop_score=0, order_id=None, is_delete=0):
        """
        评论
        # 1. id
        # 2. shop_id
        # 3. user_id
        # 4. content 评论内容
        # 5. update_content 修改后的评论内容
        # 6. create_time 评论时间
        # 7. status 0 待审核 1 审核 2 拒绝
        # 8. update_time 修改时间
        # 10. shop_score 评分
        # 11. order_id
        # 12. is_delete 0 未删除 1 删除
        """
        self.id = id
        self.shop_id = shop_id
        self.user_id = user_id
        self.content = content
        self.update_content = update_content
        self.create_time = create_time
        self.status = status
        self.update_time = update_time
        self.shop_score = shop_score
        self.order_id = order_id
        self.is_delete = is_delete
