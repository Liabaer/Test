# -*- coding: utf-8 -*-
import datetime
import random
from study_project.test_api.test_public import Job

class Order(object):
    def __init__(self, order_id='', distance='', order_price=0.00, courier_id='',
                 order_status='', delivery_fee=0.00, user_location='', shop_location='', create_time='', accepted_time='',completed_time=''):
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
        self.order_id = order_id
        self.distance = distance
        self.order_price = order_price
        self.courier_id = courier_id
        self.order_status = order_status
        self.delivery_fee = delivery_fee
        self.user_location = user_location
        self.shop_location = shop_location
        self.create_time = create_time
        self.accepted_time = accepted_time
        self.completed_time = Job.get_time()


    def create_order(self, order_price=0.00, order_status='pending'):
        """
        1. 初始化函数 （即创建订单函数，入参如下，
        创建时间为当前系统时间（调用工具类的获取当前时间）
        、订单id随机11位数字、订单状态pending, 支付价格、用户经纬度、商家经纬度，配送距离由经纬度调用公共类计算，其他字段默认为空。
        :return:
        """
        self.create_time = Job.get_time()
        for i in range(11):
            self.order_id = self.order_id + random.randint(0, 9)
        self.user_location = '131.4547,1.474'
        x = self.user_location.split(',')
        self.shop_location = '131.9999,1.999'
        y = self.shop_location.split(',')
        self.distance = Job.distance_haversine_simple(x[0], x[0], y[0], y[1])


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