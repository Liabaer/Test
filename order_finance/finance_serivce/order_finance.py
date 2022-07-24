# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from order_finance.finance_serivce.settle_account_service import SettleAccountService
from order_finance.finance_serivce.user_service import UserService
from study_project.test_api.test_public import Job


class OrderFinanceService(object):
    @staticmethod
    def place_order(amount, user_token):
        """
        下单
        :param amount:
        :param user_token:
        :return:
        """
        user_id = RedisClient.create_redis_client().get("user_token_" + str(user_token))
        if user_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            #将数据写入到订单表中
            db.execute("insert into order_finance(amount, status,user_id, create_time) values (%s,%s,%s,%s)",
                       (amount, 0, user_id, Job.get_time()))
            connection.commit()
            # 调用订单结算服务类的新增结算订单的方法
            #   传入的amount为用户下单金额的30%，保留2位小数
            order_id = db.lastrowid
            new_amount = round(amount*0.3, 2)
            SettleAccountService.add_settle_account(order_id, new_amount)

            # 调用用户的消费函数
            UserService.user_consumer(user_id, amount)


    @staticmethod
    def accepted_order(order_id,courier_token):
        """
        接单
        :param order_id:
        :param courier_token:
        :return:
        """
        courier_id = RedisClient.create_redis_client().get("courier_token_" + str(courier_token))
        if courier_id is None:
            print("骑手未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            # 修改订单表的数据（courier_id和status字段）
            db.execute("update order_finance set courier_id=%s,status=%s where id=%s", (courier_id, 1, order_id))
            connection.commit()
            print("接单成功")


    @staticmethod
    def completed_order(order_id,courier_token):
        courier_id = RedisClient.create_redis_client().get("courier_token_" + str(courier_token))
        if courier_id is None:
            print("骑手未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            # 修改订单表的数据（courier_id和status字段）
            db.execute("update order_finance set courier_id=%s,status=%s where id=%s", (courier_id, 2, order_id))
            connection.commit()
            # 调用订单结算服务类的结算订单方法
            SettleAccountService.settle_account(order_id,courier_id)