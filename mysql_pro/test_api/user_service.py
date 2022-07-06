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


class UserService(object):

    @staticmethod
    def register_user(user):
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
