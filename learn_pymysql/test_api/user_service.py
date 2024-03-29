# -*- coding: utf-8 -*-
import random

import pymysql.cursors

from learn_pymysql.test_api.coupon import Coupon
from learn_pymysql.test_api.coupon_service import CouponService
from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job
from learn_pymysql.test_api.verification_code import VerificationCode
from learn_pymysql.test_api.verification_code_service import VerificationCodeService
from learn_pymysql.test_api.order_service import OrderService
from learn_pymysql.test_api.mysql_order import MysqlOrder


class UserService(object):

    @staticmethod
    def password_check(s):
        """
        判断密码合法性
        :param s:
        :return:
        """
        flagA = False
        flagB = False
        for x in s:
            # 判断是否为纯数字
            if x.isdigit():
                flagA = True
            # 判断是否为纯字母
            elif x.isalpha():
                flagB = True
            else:
                return False
        if flagA and flagB:
            return True
        return False

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
        if not (5 < len(user.name) < 10):
            print("姓名校验不通过")
        elif not (5 < len(user.email) < 100):
            print("邮箱校验不通过")
        elif not (5 < len(user.phone_number) < 10):
            print("手机号校验不通过")
        # 他的时候判断有没有不满足条件的x，放进数组里，如果数组大于0，说明有不满足条件的
        elif not UserService.password_check(user.password) or len(user.password) < 5:
            # elif len([x for x in user.password if not x.isalnum()]) > 0 or len(user.password) < 5:
            # 不能这样写啊喂
            # elif 5 > len(user.password) or (x for x in user.password).isalnum() == False
            # or (x for x in user.password).isalnum() == False:
            print("密码校验不通过")
        else:
            db.execute(
                "insert into user(name,email,phone_number,password,amount,create_time,is_login,last_login_time) "
                "values(%s,%s,%s,%s,%s,%s,%s,%s) ",
                (user.name, user.email, user.phone_number, user.password, user.amount, user.create_time, user.is_login,
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
        db.execute("select * from user where `name` = %s and password=%s", (user_name, pwd))
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
            while i < 15:
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
            # 这个res就是这个缓存key的values，就是id 所以不需要单独处理
            # json.load(res)
            # res_id = res
            db.execute("select * from user where id = %s", res)
            user = db.fetchone()
            if user['password'] != pwd:
                print("密码输入错误")
            elif len([x for x in new_pwd if not (x.isalpha() or x.isalnum())]) > 0 or len(new_pwd) < 5:
                print("密码校验不通过")
            else:
                # 调用验证码服务
                code = VerificationCode(email=user['email'])
                VerificationCodeService.verification_code(code)
                flag = VerificationCodeService.check_code(code.email, code.email_code)
                if flag:
                    VerificationCodeService.use_code(code.email, code.email_code)
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
            db.execute("update user set last_login_time = %s,is_login=%s where id = %s", (Job.get_time(), 0, res))
            connection.commit()

    @staticmethod
    def add_user_address(token, location, addr_text):
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
            db.execute(
                "insert into user_address(address_location,address_text,user_id,create_time) values (%s,%s,%s,%s)",
                (location, addr_text, res, Job.get_time()))
            connection.commit()

    @staticmethod
    def user_recharge(token, amount):
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
            db.execute("select amount from user where id = %s", user_id)
            amount_old = db.fetchone()
            db.execute("update user set amount = %s where id = %s", (amount + amount_old['amount'], user_id))
            connection.commit()

    @staticmethod
    def place_order(token, user_addr_id, shop_id, item_dict: dict, coupon_id):
        """
        用户下单
        :param token:
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
            db.execute("select * from user where id = %s", user_id)
            user = db.fetchone()
            db.execute("select * from shop where id = %s", shop_id)
            shop_info = db.fetchone()
            shop_status = shop_info['status']
            # print(shop_status)
            shop_location = shop_info['address_location']
            x1 = shop_location.split(',')[0]
            x2 = shop_location.split(',')[1]
            db.execute("select * from user_address where id = %s", user_addr_id)
            user_info = db.fetchone()
            user_location = user_info['address_location']
            y1 = user_location.split(',')[0]
            y2 = user_location.split(',')[1]
            # 获取用户到商家经纬度
            distance = Job.distance_haversine_simple(x1, x2, y1, y2)
            if shop_status == 1:
                print("商家未营业")
            elif distance > 10000:
                print("距离太远")
            else:
                # 查询商品表计算每个商品的价格，然后根据字典里的次数，统计出总价
                item_amount = 0
                for k, v in item_dict.items():
                    db.execute("select * from item where id = %s", k)
                    k_info = db.fetchone()
                    k_price = k_info['price']
                    k_count = k_info['count']
                    item_amount += k_price * v
                    # 需要更新商品表的数据，将每个商品的库存减去购买的量（循环update)
                    db.execute("update item set count=%s where id=%s", (k_count - v, k))
                    connection.commit()
                # 根据couponid查询出coupon
                db.execute("select * from coupon where id=%s", coupon_id)
                temp = db.fetchone()
                # 通过查询的temp字典新建一个coupon对象
                coupon = Coupon(id=temp['id'], coupon_price=temp['coupon_price'],
                                coupon_discount=temp['coupon_discount'], type=temp['type'],
                                create_time=temp['create_time'])
                # 调用优惠券服务类，计算优惠价格（传入coupon对象，和计算出的商品价格）
                coupon_amount = CouponService.cal_price(coupon, item_amount)
                # 实际商品价格=商品原价-优惠价格
                real_amount = item_amount - coupon_amount
                if user['amount'] < real_amount:
                    print("金额不足")
                else:
                    order = MysqlOrder(order_price=real_amount, distance=distance, user_location=user_location,
                                       shop_location=shop_location, user_id=user_id, user_email=user['email'])
                    # 调用下单函数
                    OrderService.insert_order(order)
                    # 查询出用户原来余额
                    db.execute("select amount from user where id = %s", user_id)
                    amount_old = db.fetchone()
                    # 更新用户余额
                    db.execute("update user set amount = %s where id = %s",
                               (amount_old['amount'] - real_amount, user_id))
                    connection.commit()

    @staticmethod
    def delete_order(token, order_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from `order` where id = %s", order_id)
        res = db.fetchone()
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        elif res['status'] == 'completed':
            print("订单无法取消")
        elif res['courier_id'] is not None:
            OrderService.cancel_order(order_id)
            OrderService.delete_order(order_id, user_id)
            print("订单" + str(order_id) + "删除成功")
        else:
            OrderService.delete_order(order_id, user_id)
            print("订单" + str(order_id) + "删除成功")
