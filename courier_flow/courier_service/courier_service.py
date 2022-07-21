# -*- coding: utf-8 -*-
import random

import pymysql.cursors

from courier_flow.courier_service.vaild_check import ValidCheckUtils
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient


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
        if not ValidCheckUtils.check_phone(courier.phone_number):
            print("手机号不合法")
        elif not (ValidCheckUtils.is_en_num(courier.id_card) and ValidCheckUtils.is_between(courier.id_card, 0, 28)):
            print("id_card不合法")
        elif not (ValidCheckUtils.is_between(courier.password, 5, 10)):
            print("密码不合法")
        else:
            #  判断name是否只包含英文名，如果包含其他字符，则过滤，过滤完字符串不允许为空
            if ValidCheckUtils.is_en(courier.name):
                db.execute(
                    "insert into courier_audit_model(name, status, create_time, phone_number, password, is_ready, id_card) values (%s,%s,%s,%s,%s,%s,%s)",
                    (courier.name, courier.status, courier.phone_number, courier.password, courier.is_ready,
                     courier.id_card))
                connection.commit()
                # 调用审核表的新增审核记录函数
            else:
                str = ''
                for i in courier.name:
                    if i.isalpha() is False:
                        continue
                    else:
                        str += i
                if str == '':
                    print("name不合法")
                else:
                    db.execute(
                        "insert into courier_audit_model(name, status, create_time, phone_number, password, is_ready, id_card) values (%s,%s,%s,%s,%s,%s,%s)",
                        (courier.name, courier.status, courier.phone_number, courier.password, courier.is_ready,
                         courier.id_card))
                    connection.commit()
                    # 调用审核表的新增审核记录函数

    @staticmethod
    def courier_login(phone_number, password):
        """
        登录
        :param phone_number:
        :param password:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if not ValidCheckUtils.check_phone(phone_number):
            print("手机号不合法")
        elif not (ValidCheckUtils.is_between(password, 5, 10)):
            print("密码不合法")
        else:
            db.execute("select * from courier_audit_model where phone_number=%s and password=%s")
            courier_res = db.fetchone()
            if courier_res is None:
                print("电话号码或密码输入错误")
            else:
                # 登录成功
                token_res = RedisClient.create_redis_client().get("courier_login_id_" + courier_res['id'])
                if token_res == '':
                    # 登录成功返回token(token为15位英语+数字字符串)
                    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "
                    token = ''
                    for i in range(14):
                        token += random.choice(s)
                    # key是courier_login_id_{courier_id} value是token
                    RedisClient.create_redis_client().set("courier_login_id_" + courier_res['id'], token, ex=86400)
                    # key是courier_login_token_{token} value是courier_id
                    RedisClient.create_redis_client().set("courier_login_token_" + str(token), courier_res['id'],
                                                          ex=86400)
                    return token
                else:
                    # 判断redis中key courier_login_id_{courier_id}是否存在
                    print("开始执行单点登录，退出前一次登录")
                    # 删除courier_login_id_{courier_id}
                    RedisClient.create_redis_client().delete("courier_login_id_" + courier_res['id'])
                    # courier_login_token_{token}
                    RedisClient.create_redis_client().delete("courier_login_token_" + str(token_res))

    @staticmethod
    def get_courier(token):
        """
        获取骑手信息
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        courier_id = RedisClient.create_redis_client().get("courier_login_token_" + str(token))
        if courier_id is None:
            print("骑手未登录")
        else:
            db.execute("select * from courier_audit_model where id = %s", courier_id)
            res = db.fetchone()
            courier_info = {'id': res['id'], 'phone_number': res['phone_number'], 'name': res['name'],
                            'is_ready': res['is_ready']}
            return courier_info
