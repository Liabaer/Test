# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job


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
        if user_id is None:
            print("用户未登录")
        elif user_id['type'] == 0:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            # 将数据写入到订单表中
            db.execute("insert into order_new(user_id, status) values (%s,%s,%s)",
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
            for courier in courier_res:
                # 3. 将send_time大于当前时间5分钟的订单status修改为超时，并且记录过期时间
                if (Job.get_time() - courier['send_time']).total_seconds()/60 >= 5:
                    db.execute("update order_pool_notification set status = %s,timeout_time=%s where courier_id=%s",
                               (2, Job.get_time(), courier['courier_id']))
                else:
                    # 4. 将未超时的订单返回
                    # 1. 返回数据是个数组
                    # 2. 数组里每个元素是字典
                    # 3. 字典中有订单id,send_time
                    res_dict = {'order_id': courier['order_id'], 'send_time': courier['send_time']}
                    res_list.append(res_dict)
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
            # 修改订单表的数据
            db.execute("update order_new set courier_id=%s,status=%s where id=%s", (courier_id, 1, order_id))
            print("接单成功")

            # 3. 修改订单分配表的数据
            # （这里需要注意假设订单a分给了b,c,d三个人 b接单了除了要修改b这条订单分配表，c和d的订单分配表的数据也需要修改）
            db.execute("update order_pool_notification set status = %s,accepted_time=%s where courier_id=%s",
                       (1, Job.get_time(), courier_id))
            # 查询所有待分配订单
            db.execute("select * from order_pool_notification where order_id=%s", order_id)
            order_pool = db.fetchall()
            for order in order_pool:
                # 修改其它待分配数据未未抢到
                if order_pool['status'] == 0:
                    db.execute("update order_pool_notification set status = %s,un_accepted_time=%s where order_id=%s",
                               (3, Job.get_time(), order['order_id']))
                else:
                    continue
            connection.commit()


