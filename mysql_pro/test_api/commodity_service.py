# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job


class CommodityService(object):
    @staticmethod
    def create_commidity(price, count, shop_id, token):
        """
        创建商品
        :param price:
        :param count:
        :param shop_id:
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
            db.execute("select * from user where id = %s", (user_id))
            user = db.fetchone()
            if user['type'] != 'admin':
                print("权限不足")
            else:
                # 将商品写入到表中
                db.execute("insert into item(price,count,shop_id,create_time) values (%s,%s,%s,%s)",(price,count,shop_id,Job.get_time()))
                connection.commit()

    @staticmethod
    def add_count(shop_id,count,token):
        """
        添加库存
        :param shop_id:
        :param count:
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
            db.execute("select * from user where id = %s", (user_id))
            user = db.fetchone()
            if user['type'] != 'admin':
                print("权限不足")
            else:
                db.execute("select * from item where shop_id=%s", (shop_id))
                old_count = db.fetchone()['count']
                # 则将增加的库存，存到表中
                db.execute("update item set count=%s where shop_id = %s",(old_count+count,shop_id))
                connection.commit()

    @staticmethod
    def update_price(shop_id, price, token):
        """
        修改定价
        :param shop_id:
        :param price:
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
            db.execute("select * from user where id = %s", (user_id))
            user = db.fetchone()
            if user['type'] != 'admin':
                print("权限不足")
            else:
                # 将定价修改为price
                db.execute("update item set price=%s where shop_id = %s", (price, shop_id))
                connection.commit()
