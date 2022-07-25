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
            print("类型达咩")

    @staticmethod
    def accepted_order(user_token, courier_id, order_id):
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
                # 修改订单表的数据
                db.execute("update order_new set courier_id=%s,status=%s where id=%s", (courier_id, 1, order_id))
                connection.commit()
                print("接单成功")
                # 3. 将数据写入订单分配记录表
                db.execute(
                    "insert into order_pool_notification(courier_id, order_id, send_time, status, admin_id, timeout_time, accepted_time, un_accepted_time) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (courier_id, order_id, Job.get_time(), 1, user_id, '', Job.get_time(), ''))
                connection.commit()
            else:
                print("类型不符合")
