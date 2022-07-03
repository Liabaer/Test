# -*- coding: utf-8 -*-
class MysqlOrder(object):
    def __init__(self, id='',order_price=0, courier_id='', user_location='', shop_location='',distance='', start_delivery_time='', user_email='',assign_type=0):
        """
        1. id
        2. user_location
        3. shop_location
        4. distance 用户距离商家的直线距离
        5. order_price 订单的总价
        6. courier_id 骑手id
        7. status 订单的状态（pending, accepted, delivering, completed)
        8. delivery_fee 配送费(接单后计算)
        9. create_time 订单生成时间
        10. accepted_time 接单时间
        11. start_delivery_time 开始配送时间
        12. completed_time 完成时间
        13. user_email 骑手邮件
        14.assign_typ 0人工分单，1自动分单

        """
        self.id = id
        self.user_location = user_location
        self.shop_location = shop_location
        self.distance = distance
        self.order_price = order_price
        self.courier_id = courier_id
        self.order_status = 'pending'
        self.delivery_fee = 0.00
        self.create_time = ''
        self.accepted_time = ''
        self.completed_time = ''
        self.start_delivery_time = start_delivery_time
        self.user_email = user_email
        self.assign_type = assign_type