# -*- coding: utf-8 -*-
import random

import pymysql

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job
from learn_pytest.test_ordering.ordering_service.vaild_check import ValidCheckUtils


class CustomerService(object):
    @staticmethod
    def create_customer(customer):
        """
        创建顾客
        :param customer:（入参 顾客对象）
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 1. 密码必须包含数字和字母，长度为8-15位，提示密码不合法
        if not (ValidCheckUtils.is_en_num(customer.password) and ValidCheckUtils.is_between(customer.password, 8, 15)):
            print("密码不合法")
            return False
        else:
            # 2. 姓名必须唯一，如果存在则提示姓名存在，返回false
            db.execute("select * from customer_review_user where name=%s", customer.name)
            if db.fetchone() is not None:
                print("姓名已存在")
                return False
            else:
                # 3. 满足以上条件插入用户表数据
                db.execute("insert into customer_review_user(amount, name, password, create_time) values (%s,%s,%s,%s)",
                           (customer.amount, customer.name, customer.password, Job.get_time()))
                connection.commit()
                return True

    @staticmethod
    def customer_login(name, password):
        """
        登录（入参name,password)
        :param name:
        :param password:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from customer_review_user where name=%s and password=%s", (name, password))
        if db.fetchone() is None:
            # login_fail_{name}_{password},value为失败的次数比如1，过期时间一天，提示用户名密码错误
            # RedisClient.create_redis_client().set("login_fail_" + name + "_" + password, 1, ex=24 * 60 * 60)
            count = RedisClient.create_redis_client().get("login_fail_" + name + "_" + password)
            # 需要先判断count是不是None，不然后续要变错
            if count is None:
                RedisClient.create_redis_client().set("login_fail_" + name + "_" + password, 1, ex=24 * 60 * 60)
            elif int(count) >= 10:
                print("当天无法登录")
            else:
                count = int(count) + 1
                RedisClient.create_redis_client().set("login_fail_" + name + "_" + password, count, ex=24 * 60 * 60)
            print("用户名密码错误")
        else:
            s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "
            token = ''
            for i in range(14):
                token += random.choice(s)
            RedisClient.create_redis_client().set("user_login" + str(token), name, ex=24 * 60 * 60)
            print("登陆成功")
            return token

    @staticmethod
    def charge(amount, token, type):
        """
        充值/消费（入参amount,token,type)
        :param amount:
        :param token:
        :param type:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        name = RedisClient.create_redis_client().get('user_login' + str(token))
        # 消费
        if name is None:
            print("用户未登录")
        else:
            db.execute("select * from customer_review_user where  name= %s", name)
            old_amount = db.fetchone()
            # 2. type等于1消费amount元
            if type == 1 and old_amount['amount'] < amount:
                print("余额不足")
            elif type == 1 and old_amount['amount'] >= amount:
                db.execute("update customer_review_user set amount=%s where name=%s",
                           (old_amount['amount'] - amount, name))
                connection.commit()
                print("消费成功")
            #  1. type等于0充值amount元
            elif type == 0:
                db.execute("update customer_review_user set amount=%s where name=%s",
                           (old_amount['amount'] + amount, name))
                connection.commit()
                print("充值成功")
            else:
                print("未知的参数")
