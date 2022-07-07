# -*- coding: utf-8 -*-
import json
import random

import pymysql.cursors

from mysql_pro.test_api.user import User
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.email_utils import SendEmail
from study_project.test_api.test_public import Job
from mysql_pro.test_api.verification_code import VerificationCode
from mysql_pro.test_api.verification_code_service import VerificationCodeService
from mysql_pro.test_api.order_service import OrderService
from mysql_pro.test_api.mysql_order import MysqlOrder


class UserService(object):

    @staticmethod
    def register_user(user):
        """
        注册用户
        :param user:
        :return:
        """
        flag = False
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if 5 > len(user.name) > 10:
            print("姓名校验不通过")
        elif 5 > len(user.email) > 100:
            print("邮箱校验不通过")
        elif 5 > len(user.phone_number) > 10:
            print("手机号校验不通过")
        # 他的时候判断有没有不满足条件的x，放进数组里，如果数组大于0，说明有不满足条件的
        elif len([x for x in user.password if not (x.isalpha() or x.isalnum())]) > 0 or len(user.password) < 5:
            # 不能这样写啊喂
            # elif 5 > len(user.password) or (x for x in user.password).isalnum() == False or (x for x in user.password).isalnum() == False:
            print("密码校验不通过")
        else:
            db.execute(
                "insert into user(name,email,phone_number,password,amount,create_time,is_login,last_login_time) values(%s,%s,%s,%s,%s,%s,%s,%s) ",
                (user.name, user.email, user.phone_number, user.password, user.amount, user.create_time,user.is_login,
                 user.last_login_time))
            connection.commit()
            flag = True
        if flag:
            print("注册成功")
            # # 发送邮件通知用户注册成功
            # SendEmail.send_msg_email(receive_name=user.email.split('@')[0],
            #                          receive_email=[user.email],
            #                          title='骑手注册成功', note='于' + user.create_time + '时间注册成功')

            return True
        else:
            return False

    @staticmethod
    def user_login(user_name, pwd):
        """
        登陆
        :param user_name:
        :param pwd:
        :return:
        """
        # flag = False
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from user where name = %s and password=%s", (user_name,pwd))
        res = db.fetchone()
        if res is None:
            print('用户名或者密码错误')
            return None
        elif res['is_login'] == 1:
            print("用户已经登录")
            return None
        else:
            db.execute("update user set is_login=%s where name = %s", (1, user_name))
            connection.commit()
            flag = True
            print("登陆成功")
            token = ''
            i = 0
            while i != 15:
                token += chr(random.randint(ord('a'), ord('z')))
                i += 1
                token += str(random.randint(0, 9))
                i += 1
                # i += 2
            RedisClient.create_redis_client().set("user_login_cache_" + str(token), res['id'])
            return token

    @staticmethod
    def update_pwd(token, pwd, new_pwd):
        """
        修改密码
        :param token:
        :param pwd:
        :param new_pwd:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 这个res就是这个缓存key的values，就是id  RedisClient.create_redis_client().set("user_login_cache_" + str(token), res['id'])
        res = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if res is None:
            print("用户未登录")
        else:
            #这个res就是这个缓存key的values，就是id 所以不需要单独处理
            # json.load(res)
            # res_id = res
            db.execute("select * from user where id = %s", (res))
            user = db.fetchone()
            if user['password'] != pwd:
                print("密码输入错误")
            elif len([x for x in new_pwd if not (x.isalpha() or x.isalnum())]) > 0 or len(new_pwd) < 5:
                print("密码校验不通过")
            else:
                # 调用验证码服务
                code = VerificationCode(email=user['email'])
                VerificationCodeService.verification_code(code)
                flag = VerificationCodeService.check_code(code.email,code.email_code)
                if flag:
                    VerificationCodeService.use_code(code.email,code.email_code)
                    db.execute("update user set password = %s where id = %s", (new_pwd, res))
                    connection.commit()
                else:
                    print("验证码错误")

    @staticmethod
    def login_out(token):
        """
        退出登录
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        res = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if res is None:
            print("用户未登录")
        else:
            RedisClient.create_redis_client().delete("user_login_cache_" + str(token))
            # res_id = json.loads(res)['id']
            db.execute("update user set last_login_time = %s where id = %s", (Job.get_time(), res))

    @staticmethod
    def add_user_address(token,location,addr_text):
        """
        添加用户地址
        :param token:
        :param location:
        :param addr_text:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        res = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if res is None:
            print("用户未登录")
        else:
            db.execute("insert into user_address(address_location,address_text,create_time) values (%s,%s,%s)",(location,addr_text,Job.get_time()))
            connection.commit()

    @staticmethod
    def user_recharge(token,amout):
        """
        用户充值
        :param token:
        :param amout:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            db.execute("select amount from user where id = %s", (user_id))
            amount_old = db.fetchone()
            db.execute("update user set amount = %s where id = %s", (amout+amount_old, user_id))
            connection.commit()


    @staticmethod
    def place_order(token,sale_amount,user_addr_id,shop_id):
        """
        用户下单
        :param token:
        :param sale_amount:
        :param user_addr_id:
        :param shop_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            db.execute("select * from user where id = %s", (user_id))
            user = db.fetchone()
            db.execute("select * from shop where id = %s", (shop_id))
            shop_status = db.fetchone()['status']
            shop_location = db.fetchone()['address_location']
            x1 = shop_location.split(',')[0]
            x2 = shop_location.split(',')[1]
            db.execute("select * from user_adrress where id = %s", (user_addr_id))
            user_location = db.fetchone()['address_location']
            y1 = user_location.split(',')[0]
            y2 = user_location.split(',')[1]
            # 获取用户到商家经纬度
            distance = Job.distance_haversine_simple(x1,x2,y1,y2)
            if user['amount'] < sale_amount:
                print("金额不足")
            elif shop_status == 1:
                print("商家未营业")
            elif distance > 10000:
                print("距离太远")
            else:
                order = MysqlOrder(order_price=sale_amount,distance=distance,user_location=user_location,shop_location=shop_location,user_id=user_id,status='pending',create_time=Job.get_time())
                OrderService.insert_order(order)
                db.execute("select amount from user where id = %s", (user_id))
                amount_old = db.fetchone()
                db.execute("update user set amount = %s where id = %s", (amount_old-sale_amount, user_id))
                connection.commit()

    @staticmethod
    def delete_order(token, order_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from `order` where id = %s", (order_id))
        res = db.fetchone()
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        elif res['status'] == 'completed':
            print("订单无法取消")
        elif res['courier_id'] is not None:
            OrderService.cancel_order(order_id)
            OrderService.delete_order(order_id,user_id)
            print("订单" + str(order_id) + "删除成功")

