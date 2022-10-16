# -*- coding: utf-8 -*-
import random

import pymysql

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job
from learn_project.web_project.web_api.vaild_check import ValidCheckUtils


class UserService(object):
    @staticmethod
    def user_login(user):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from new_user where phone_number=%s", user.phone_number)
        temp = db.fetchone()
        if temp is None:
            print("用户名错误")
        else:
            if temp['password'] == user.password:
                print("登陆成功")
                s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "
                token = ''
                for i in range(14):
                    token += random.choice(s)
                RedisClient.create_redis_client().set("user_is_login" + token, temp['id'], ex=86400)
                return token
            else:
                print("密码错误")

    @staticmethod
    def user_register(user):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if ValidCheckUtils.is_num(user.phone_number) and ValidCheckUtils.is_between(user.phone_number, 10,
                                                                                    15) and ValidCheckUtils.is_en_num(
            user.password) and ValidCheckUtils.is_between(user.password, 5, 10):
            db.execute("insert into new_user(phone_number,password,create_time) values(%s,%s,%s)",
                       (user.phone_number, user.password, Job.get_time()))
            connection.commit()
            print("注册成功")
        else:
            print("用户名或密码校验不通过")
