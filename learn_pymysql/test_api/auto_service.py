# -*- coding: utf-8 -*-
import pymysql.cursors

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.courier_service import CourierService
from learn_pymysql.test_api.mysql_Courier import MySQLCourier
from learn_pymysql.test_api.mysql_order import MysqlOrder
from learn_project.my_project.test_api.test_public import Job


class AutoService(object):
    @staticmethod
    def auto_service():
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 1. 查找order表里面状态是待分配的订单，以及assign_type是1的订单，组成成订单列表
        db.execute("select * from `order` where status=%s and assign_type=%s", ('pending', 1))
        res = db.fetchall()
        order_list = [x for x in res]
        #  2. 查找在线骑手列表（从redis中读取）
        # 1. 根据骑手服务类的获取在线配送员列表（函数返回的是courier_id1,courier_id2,courier_id3这样的数据）
        # 2. 根据骑手服务类的在线配送员获取详情（上面的每个配送员id获取配送员的详情，组装成一个在线骑手详情列表）
        temp = CourierService.get_courier_online()
        courier_online = temp.split(',')
        courier_list = []

        for courier in courier_online:
            courier_online_cache = CourierService.get_courier_info(courier)
            courier_list.append(courier_online_cache)

        # 1. 找到对于每个订单来说最近的那个骑手(最近指的是订单的商家距离到骑手距离最近），并且满足以下条件则直接分配订单
        # 1. 未完成订单数小于5（这里要查询骑手的未完成订单缓存）
        # 2. 骑手距离用户距离小于5000米
        # 3. 骑手在线（骑手肯定是在线的所以不用判断）
        # 4. 骑手的delivery_type为delivery
        # 5. 满足以上条件，则调用接单
        for j in order_list:
            order = MysqlOrder(id=j['id'], user_location=j['user_location'], shop_location=j['shop_location'])
            y1 = order.shop_location.split(',')[0]
            y2 = order.shop_location.split(',')[1]
            z1 = order.user_location.split(',')[0]
            z2 = order.user_location.split(',')[1]
            min_distance = 5000
            min_courier = ''
            flag = False
            for i in courier_list:
                courier = MySQLCourier(id=i['id'], courier_email=i['courier_email'], create_time=i['create_time'],
                                       delivery_type=i['delivery_type'], courier_location=i['courier_location'],
                                       status='online')
                x1 = courier.courier_location.split(',')[0]
                x2 = courier.courier_location.split(',')[1]
                shop_distance = Job.distance_haversine_simple(x1, x2, y1, y2)
                user_distance = Job.distance_haversine_simple(x1, x2, z1, z2)
                temp = CourierService.get_uncompleted_order(courier)
                courier_uncomplete_order = temp.split(',')
                if len(courier_uncomplete_order) > 5:
                    print('未完成订单数超过5')
                    continue
                elif courier.delivery_type != 'delivery':
                    print('骑手配送方式不匹配')
                    continue
                elif user_distance > 5000:
                    print('骑手距离用户距离大于5000米')
                    continue
                if shop_distance < min_distance:
                    min_distance = shop_distance
                    # 这里是要等于对象courier
                    min_courier = courier
                    flag = True

            if flag:
                print('找到骑手')
                CourierService.get_order(min_courier, order.id)
            else:
                # 6. 如果订单没有找到任何骑手，则将订单的assign_type修改为0
                print('订单id' + str(order.id) + '未找到骑手进入人工分单')
                db.execute("update `order` set assign_type=%s where id =%s", (0, order.id))
                connection.commit()
