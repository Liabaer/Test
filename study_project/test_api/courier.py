# -*- coding: utf-8 -*-
# 1. 定义一个骑手类Courier
import random

from study_project.test_api.test_public import Job

class Courier(object):

    def __init__(self, courier_id='', location='', status='', uncompleted_order_id='', delivery_type='',comleted_order_id=''):
        """
        1. 骑手id
        2. 骑手经纬度（逗号分割 lng,lat)
        3. 骑手状态 （online，offline)
        4. 骑手未完成订单id列表 （订单id逗号分割）
        5. 骑手类型 （delivery,shop_deliver)
        6. 已完成订单列表 （订单id逗号分割）
        :param courier_id:
        :param location:
        :param status:
        :param uncompleted_order_id:
        :param delivery_type:
        """
        self.courier_id = id
        self.location = ''
        self.status = ''
        self.uncompleted_order_id = ''
        self.delivery_type = ''
        self.comleted_order_id = ''

    def be_courier(self, courier_id='',courier_location='131.1111,1.111',status='offline',delivery_type='delivery',uncompleted_order_id=''):
        """
        1. 初始化方法 （即创建骑手，入参如下 骑手id随机五位数字，骑手经纬度写死，骑手状态offline，骑手类型delivery,未完成列表为空字符串）
        :return:
        """
        for i in range(5):
            self.courier_id += random.randint(0,9)

    def get_xy(self):
        """
        获取骑手经纬度
        :return:
        """
        return self.location

    def update_xy(self, new_location=''):
        """
        修改骑手经纬度
        :param new_location:
        :return:
        """
        self.location = new_location
        return self.location

    def is_online(self):
        """
        判断骑手是否在线
        :return:
        """
        if self.status == 'online':
            return True


    def update_status(self):
        """
        4. 修改骑手状态（切换上下线）
        :return:
        """
        if self.status == 'online':
            self.status = 'offline'
        if self.status == 'offline':
            self.status = 'online'
        return self.status


    def get_uncompleted_order_list(self):
        """
        获取骑手未完成订单数
        :return:
        """
        list_lenth = self.uncompleted_order_id.split(',')
        return len(list_lenth)

    def get_order(self,user_location='', order_id=''):
        """
        接单函数（满足以下条件则接单）（传入参数用户经纬度，订单id）
        1. 骑手状态等于online
        2. 未完成订单数小于3
        3. 距离用户小于3000米直线距离
        4. 骑手类型等于delivery
        5. 满足以上条件则接单，把新订单id，写入到骑手未完成列表中
        6. 打印接单成功订单id：xxx, 否则打印接单失败，并且输出具体的失败原因（比如距离大于3000米）
        :param user_location: 传入经纬度
        :param order_id:
        :return:
        """
        x = user_location.split(',')
        y = self.location.split(',')
        distance = Job.distance_haversine_simple(x[0],x[1],y[0],y[1])
        if self.status != 'online':
            print('接单失败,骑手未上线')
        elif self.get_uncompleted_order_list() > 3:
            print('接单失败,未完成订单数量大于3')
        elif self.delivery_type == 'delivery':
            print('接单失败,骑手类型不匹配')
        elif distance > 3000:
            print('接单失败,距离大于3000米')
        else:
            self.uncompleted_order_id = self.uncompleted_order_id + order_id
            print('接单成功，接单ID为' + order_id)


    def completed_order(self, order_id=''):
        """
        完成订单函数 （传入需要完成的订单id)
        1. 骑手状态等于online
        2. 如果未完成订单列表存在订单id
        3. 满足以上条件则完成订单，并且将订单id从未完成列表中删除
        4. 成功打印完成订单id:xxxx 否则打印完成订单失败（不存在该订单）
        :param order_id:
        :return:
        """
        if self.status == 'online' and self.get_uncompleted_order_list() != 0:
            order_list = self.uncompleted_order_id.split(',')
            if order_id in order_list:
                order_list.remove(order_id)
                self.uncompleted_order_id = ','.join(order_list)
                print('完成订单id:' + order_id)
            else:
                print('不存在该订单')

    def unassign_order(self, order_id):
        """
        7. 撤单函数（传入需要撤销的订单id)
            1. 未完成订单列表存在订单id
            2. 满足以上条件则完成订单，并且将订单id从未完成列表中删除
            3. 成功打印撤销订单id:xxx 成功，否则打印撤单失败
        :param order_id:
        :return:
        """


