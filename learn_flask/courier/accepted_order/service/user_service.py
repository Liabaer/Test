# -*- coding: utf-8 -*-
import pymysql

from learn_flask.courier.accepted_order.service.vaild_check import ValidCheckUtils
from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job


class UserService(object):
    @staticmethod
    def register_user(name, password, type):
        """
        注册
        :param name:
        :param password:
        :param type:
        :return:
        """
        # 1. name
        # 1. 长度为5-8
        # 2. 并且只能包含小写字母，如果有大写字母，转换为小写
        # 3. 如果有元音字母，需要将元音字母提前比如name为bcacu, 则变成aubcc
        if not ValidCheckUtils.is_between(name, 5, 8):
            print("name长度不符合")
        elif not (ValidCheckUtils.to_lower_case_letters(name)):
            print("name不合法")
        else:
            name_1 = ValidCheckUtils.to_lower_case_letters(name)
            name_new = ValidCheckUtils.change_Location(name_1)
            # 2. 密码
            # 1. 长度在5-10之间
            # 2. 必须有小写字母
            # 3. 必须有数字
            if not ValidCheckUtils.is_between(password, 5, 10):
                print("password长度不符合")
            elif not (ValidCheckUtils.is_have_lower(password)):
                print("password不含字母")
            elif not (ValidCheckUtils.is_have_num(password)):
                print("password不含数字")
            else:
                connection = MysqlClient.get_connection()
                db = connection.cursor(pymysql.cursors.DictCursor)
                # 3. 写入用户表
                db.execute("insert into user_new(name, password, type, create_time) values (%s,%s,%s,%s)",
                           (name_new, password, type, Job.get_time()))
                connection.commit()

    @staticmethod
    def user_login(name, password):
        """
        登陆
        :param name:
        :param password:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from user_new where name =%s and password= %s", (name, password))
        user_res = db.fetchone()
        if user_res is None:
            print("用户不存在")
        else:
            # 生成14位全数字token，不允许0开头
            token = ValidCheckUtils.become_token()
            RedisClient.create_redis_client().set("user_login_token_" + str(token), user_res['id'], ex=86400)
            return token
