# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job


class CouponService(object):
    @staticmethod
    def create_coupon(coupon,token):
        """
        1. 创建优惠券（入参 优惠券对象,token）
        :param coupon:
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        db.execute("select * from user where id = %s", (user_id))
        user = db.fetchone()
        if user_id is None:
            print("用户未登录")
        elif user['type'] != 'admin':
            print("权限不足")
        else:
            # 优惠券写入到表中
            db.execute("insert into coupon(coupon_price,coupon_discount,type,create_time) values (%s,%s,%s,%s)",
                       (coupon.coupon_price, coupon.coupon_discount, coupon.type, Job.get_time()))
            connection.commit()

    @staticmethod
    def send_coupon(coupon_id, user_id,token):
        """
         2. 发放优惠券（入参优惠券id,用户id,token)
        :param coupon_id:
        :param user_id:
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id_redis = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        db.execute("select * from user where id = %s", (user_id))
        user = db.fetchone()
        if user_id_redis is None:
            print("用户未登录")
        elif user['type'] != 'admin':
            print("权限不足")
        else:
            # 写入到用户优惠券表中
            db.execute("update user_coupon set user_id = %s,create_time where coupon_id=%s",
                       (user_id,Job.get_time(),coupon_id))
            connection.commit()

    @staticmethod
    def cal_price(coupon,sal_amount):
        """
        计算优惠券优惠价格（入参优惠券对象，商品价格
        :param coupon:
        :param sal_amount:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from coupon where id = %s", (coupon.id))
        coupon_res = db.fetchone()
        # 如果type是0，则返回直接优惠金额
        if coupon_res['type'] == 0:
            return coupon.coupon_price
        # 如果type是1，则返回优惠百分比乘以商品价格（取整 四舍五入）
        else:
            return int(sal_amount*coupon.coupon_discount)

    @staticmethod
    def user_coupon(coupon_id,token):
        """
        使用优惠券（入参用户优惠券id,token)
        :param coupon_id:
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            db.execute("select * from user_coupon where coupon_id=%s",(coupon_id))
            res = db.fetchone()
            #  判断用户优惠券类表的用户id是否和token对应的user_id相等
            if res['user_id'] == user_id:
                db.execute("update user_coupon set status=%s,user_time=%s where coupon_id=%s",(1,Job.get_time(),coupon_id))
                connection.commit()
            else:
                print("用户不匹配")
