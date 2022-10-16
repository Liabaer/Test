# -*- coding: utf-8 -*-

import pymysql

from learn_flask.courier.accepted_order.service.vaild_check import ValidCheckUtils
from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job


class OrderService(object):
    @staticmethod
    def place_order(user_token):
        """
        下单
          1. 下单(入参 user_token)
            1. 判断redis中是否存user_token的key
            2. 判断用户是否为消费者
            2. 将已有的数据写入到订单表中
        :param user_token:
        :return:
        """
        user_id = RedisClient.create_redis_client().get("user_login_token_" + str(user_token))
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from user_new where id=%s", user_id)
        user = db.fetchone()
        if user_id is None:
            print("用户未登录")
        else:
            if user['type'] == 0:
                # 将数据写入到订单表中
                db.execute("insert into order_new(user_id, status) values (%s,%s)",
                           (user_id, 0))
                connection.commit()
            else:
                print("类型不符合")

    @staticmethod
    def send_order(user_token, courier_id, order_id):
        """
        分配接单
        1. 判断redis中是否存user_token的key
            2. 判断用户是否为管理员
            3. 将数据写入订单分配记录表
        :param user_token:
        :param courier_id:
        :param order_id:
        :return:
        """
        user_id = RedisClient.create_redis_client().get("user_login_token_" + str(user_token))
        if user_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            db.execute("select * from user_new where id=%s", user_id)
            user = db.fetchone()
            if user['type'] == 1:
                # 3. 将数据写入订单分配记录表
                db.execute(
                    "insert into order_pool_notification(courier_id, order_id, send_time, status, admin_id) values (%s,%s,%s,%s,%s)",
                    (courier_id, order_id, Job.get_time(), 0, user_id))
                connection.commit()
            else:
                print("类型不符合")

    @staticmethod
    def bulk_allocation(user_token, courier_id_list, order_id):
        """
        批量分配待接单
        1. 判断redis中是否存user_token的key
            2. 判断用户是否为管理员
            3. 循环将每个订单分配给的配送员记录数据写入订单分配记录表
        :param user_token:
        :param courier_id_list: 骑手id数组
        :param order_id:
        :return:
        """
        user_id = RedisClient.create_redis_client().get("user_login_token_" + str(user_token))
        if user_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            db.execute("select * from user_new where id=%s", user_id)
            user = db.fetchone()
            if user['type'] == 1:
                for courier_id in courier_id_list:
                    db.execute(
                        "insert into order_pool_notification(courier_id, order_id, send_time, status, admin_id) values (%s,%s,%s,%s,%s)",
                        (courier_id, order_id, Job.get_time(), 0, user_id))
                connection.commit()
            else:
                print("类型不符合")

    @staticmethod
    def get_courier_bulk_list(courier_token):
        """
        获取骑手待接单列表
        :param courier_token:
        :return:
        """
        # 判断redis中是否存courier_token的key
        courier_id = RedisClient.create_redis_client().get("courier_login_token_" + str(courier_token))
        if courier_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            # 查询订单分配记录表
            db.execute("select * from order_pool_notification where courier_id=%s", courier_id)
            courier_res = db.fetchall()
            res_list = []
            flag = False
            for courier in courier_res:
                # 3. 将send_time大于当前时间5分钟的订单status修改为超时，并且记录过期时间
                # 先处理时间差，要先使用datetime.strptime改成时间类型再求差
                time = ValidCheckUtils.time_diff(Job.get_time(), courier['send_time'])
                # time = (datetime.strptime(Job.get_time(), '%Y.%m.%d %H:%M:%S') - datetime.strptime(
                #     courier['send_time'], '%Y.%m.%d %H:%M:%S')).total_seconds()
                if time / 60 >= 5:
                    db.execute("update order_pool_notification set status = %s,timeout_time=%s where courier_id=%s",
                               (2, Job.get_time(), courier['courier_id']))
                    flag = True
                else:
                    # 4. 将未超时的订单返回
                    # 1. 返回数据是个数组
                    # 2. 数组里每个元素是字典
                    # 3. 字典中有订单id,send_time
                    res_dict = {'order_id': courier['order_id'], 'send_time': courier['send_time']}
                    res_list.append(res_dict)
            if flag:
                connection.commit()
            return res_list

    @staticmethod
    def accepted_order(courier_token, order_id):
        """
        接单
        :param courier_token:
        :param order_id:
        :return:
        """
        # 判断redis中是否存courier_token的key
        courier_id = RedisClient.create_redis_client().get("courier_login_token_" + str(courier_token))
        if courier_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            # 3. 修改订单分配表的数据
            # （这里需要注意假设订单a分给了b,c,d三个人 b接单了除了要修改b这条订单分配表，c和d的订单分配表的数据也需要修改）
            db.execute("update order_pool_notification set status = %s,accepted_time=%s where courier_id=%s",
                       (1, Job.get_time(), courier_id))
            # 查询所有待分配订单
            db.execute("select * from order_pool_notification where order_id=%s", order_id)
            order_pool = db.fetchall()
            for order in order_pool:
                time = ValidCheckUtils.time_diff(Job.get_time(), order['send_time'])
                if order['status'] == 0 and time <= 60:
                    # 修改订单表的数据 修改其它待分配数据且未超过1分钟的且courier_id等于传入参数
                    if order['courier_id'] == courier_id:
                        db.execute("update order_new set courier_id=%s,status=%s where id=%s",
                                   (courier_id, 1, order_id))
                        print("接单成功")
                    # 修改其它待分配数据且未超过1分钟的未未抢到
                    else:
                        db.execute(
                            "update order_pool_notification set status = %s,un_accepted_time=%s where order_id=%s",
                            (3, Job.get_time(), order['order_id']))
                else:
                    continue
            connection.commit()
