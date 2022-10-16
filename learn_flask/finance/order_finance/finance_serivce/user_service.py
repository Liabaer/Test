# -*- coding: utf-8 -*-

import pymysql

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_flask.finance.order_finance.finance_serivce.vaild_check import ValidCheckUtils
from learn_project.my_project.test_api.test_public import Job


class UserService(object):
    @staticmethod
    def register_user(user):
        """
        注册
        :param user:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if user.name != '' and user.password != '':
            db.execute("insert into user_finance(name, password, amount, create_time) values (%s,%s,%s,%s)",
                       (user.name, user.password, user.amount, Job.get_time()))
            connection.commit()
        else:
            print("用户姓名和密码为空")

    @staticmethod
    def user_login(user):
        """
        登陆
        :param user:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from user_finance where name =%s and password= %s", (user.name, user.password))
        user_res = db.fetchone()
        if user_res is None:
            print("用户不存在")
        else:
            # 生成14位全数字token，不允许0开头
            while True:
                token = ValidCheckUtils.become_token()
                if token[0] != '0':
                    print("登陆成功")
                    break
            RedisClient.create_redis_client().set("user_token_" + str(token), user_res['id'], ex=86400)
            return token

    @staticmethod
    def user_charge(token, amount):
        """
        充值
        :param token:
        :param amount:
        :return:
        """
        user_id = RedisClient.create_redis_client().get("user_token_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            db.execute("select * from user_finance where id=%s", user_id)
            old = db.fetchone()['amount']
            # 将amount累加到用户余额中
            db.execute("update user_finance set amount=%s where id=%s", (old + amount, user_id))
            connection.commit()

    @staticmethod
    def user_consumer(user_id, amount):
        """
        消费
        :param user_id:
        :param amount:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from user_finance where id=%s", user_id)
        old = db.fetchone()['amount']
        # 更新user表中的amount字段
        if old < amount:
            print("余额不足")
        else:
            db.execute("update user_finance set amount=%s where id=%s", (old - amount, user_id))
            connection.commit()
