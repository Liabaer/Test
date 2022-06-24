# -*- coding: utf-8 -*-
import datetime
import random
from study_project.test_api.test_public import Job
from study_project.test_api.email_utils import SendEmail


class Order(object):
    def __init__(self, order_price=0, courier_id='', user_location='', shop_location='',email=[],shop_tag_id=[]):
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
        self.order_status = 'pending'
        self.delivery_fee = 0.00
        self.create_time = Job.get_time()
        self.accepted_time = ''
        self.completed_time = ''
        self.email = email
        self.shop_tag_id = shop_tag_id


    def update_email(self, email):
        """
         修改邮箱
        :param email:
        :return:
        """
        self.email = email
        return self.email

    def add_shop_tag(self, tag_id):
        """
        新增商家标签id
        :param tag_id:
        :return:
        """
        if tag_id not in self.shop_tag_id:
            self.shop_tag_id.append(tag_id)
        else:
            print('该标签已经存在')

    def del_shop_tag(self, tag_id):
        """
        删除商家标签id
        :param tag_id:
        :return:
        """
        if tag_id in self.shop_tag_id:
            self.shop_tag_id.remove(tag_id)
        else:
            print('该标签不存在')



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
        SendEmail.send_msg_email(self.order_id, self.email,
                                 title='订单：'+self.order_id+'已接单',
                                 note='订单id'+self.order_id+'于'+self.accepted_time+'已接单，准备开始配送')


    def completed_order(self):
        """
        3. 完成 （入参无）
            1. 修改订单的状态为completed
            2. 修改完成时间为当前系统时间（调用工具类的获取当前时间）
        :return:
        """
        self.order_status = 'completed'
        self.completed_time = Job.get_time()
        SendEmail.send_msg_email(self.order_id, self.email,
                                 title='订单：' + self.order_id + '已完成',
                                 note='订单id' + self.order_id + '于' + self.accepted_time + '完成')

    def unassign(self):
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
