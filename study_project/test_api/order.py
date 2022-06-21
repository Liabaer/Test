# -*- coding: utf-8 -*-
import datetime
import random
from study_project.test_api.test_public import Job
from study_project.test_api.courier import Courier

class Order(object):
    def __init__(self, order_id='', distance='', order_price=10.00, courier_id='',
                 order_status='pending', delivery_fee=0, user_location = '131.4547,1.474', shop_location = '131.9999,1.999', create_time=Job.get_time(), accepted_time='',completed_time=''):
        """
        1. 私有属性
        1. 订单id
        2. 配送距离（用户到商家直线距离）
        3. 订单支付价格（float)
        4. 配送员id (接单后的骑手id)
        5. 订单状态 (pending,accepted,completed)
        6. 配送费 （接单后计算给骑手的配送费）
        7. 用户的经纬度
        8. 商家的经纬度
        9. 创建时间
        10. 接单时间
        11. 完成时间
        """
        self.order_id = ''
        for i in range(11):
            self.order_id = self.order_id + str(random.randint(0, 9))
        self.user_location = user_location
        self.shop_location = shop_location
        x = self.user_location.split(',')
        y = self.shop_location.split(',')
        self.distance = Job.distance_haversine_simple(x[0], x[0], y[0], y[1])
        self.order_price = order_price
        self.courier_id = courier_id
        self.order_status = order_status
        self.delivery_fee = Job.get_delivery_fee(distance)
        self.create_time = Job.get_time()
        self.accepted_time = ''
        self.completed_time = ''




    def accepted_order(self, courier_id='', delivery_fee=0):
        """
        2. 接单 （入参 配送员id, 配送费）
            1. 修改订单的状态为accepted
            2. 修改配送员的id
            3. 修改配送费
            4. 修改接单时间为当前系统时间（调用工具类的获取当前时间）
        :param courier_id:
        :param delivery_fee:
        :return:
        """
        self.order_status = 'accepted'
        self.courier_id = courier_id
        self.delivery_fee = delivery_fee
        self.accepted_time = Job.get_time()


    def completed_order(self):
        """
        3. 完成 （入参无）
            1. 修改订单的状态为completed
            2. 修改完成时间为当前系统时间（调用工具类的获取当前时间）
        :return:
        """
        self.order_status = 'completed'
        self.completed_time = Job.get_time()


    def unassign(self, courier_id):
        """
        4. 取消分配（入参，取消分配的配送员对象）
            1. 修改订单的状态为pending
            2. 修改配送员的id为空
            3. 修改接单时间为空
            4. 修改配送费为空
            5. 调用骑手的撤单函数
        :param courier_id:
        :return:
        """
        self.order_status = 'pending'
        self.courier_id = ''
        self.accepted_time = ''
        self.delivery_fee = ''
        Courier.unassign_order(order_id=self.order_id)