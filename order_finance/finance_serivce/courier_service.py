# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from order_finance.finance_serivce.vaild_check import ValidCheckUtils
from study_project.test_api.test_public import Job


class CourierService(object):
    @staticmethod
    def register_courier(courier):
        """
        注册
        :param courier:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if courier.name != '' and courier.password != '':
            db.execute("insert into courier_finance(name, password, amount, create_time) values (%s,%s,%s,%s)",
                       (courier.name, courier.password, courier.amount, Job.get_time()))
            connection.commit()
        else:
            print("骑手姓名和密码为空")


    @staticmethod
    def courier_login(courier):
        """
        登陆
        :param courier:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from courier_finance where name =%s and password= %s", (courier.name, courier.password))
        courier_res = db.fetchone()
        if courier_res is None:
            print("骑手不存在")
        else:
            while True:
                token = ValidCheckUtils.become_token()
                if token[0] != '0':
                    print("登陆成功")
                    break
            RedisClient.create_redis_client().set("courier_token_" + str(token), courier_res['id'], ex=86400)
            return token


    @staticmethod
    def add_amount(courier_id,amount):
        """
        新增工资
        :param courier_id:
        :param amount:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from courier_finance where id=%s", courier_id)
        old = db.fetchone()['amount']
        # 将amount累加到用户余额中
        db.execute("update user_finance set amount=%s where id=%s", (old + amount, courier_id))
        connection.commit()