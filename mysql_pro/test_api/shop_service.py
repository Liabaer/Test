# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from mysql_pro.test_api.shop import Shop
from study_project.test_api.test_public import Job


class ShopService(object):
    @staticmethod
    def create_shop(shop, token):
        """
        创建商家
        :param shop:
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
            db.execute("select * from user where id = %s", user_id)
            res = db.fetchone()
            if res['type'] != 'admin':
                print("权限不足")
            elif (for i in shop.name if i not in s):
                print("商家名称不合法")
            elif len(shop.address_text) < 10:
                print("商家地址文本太短")
            else:
                # 处理location保留6为小数
                x = str(round(int(shop.address_location.split(',')[0]), 6))
                y = str(round(int(shop.address_location.split(',')[1]), 6))
                location = x + ',' + y
                db.execute("insert into shop(name,address_text,address_location,create_time) values (%s,%s,%s,%s)",
                           (shop.name, shop.address_text, location, Job.get_time()))
                connection.commit()

    @staticmethod
    def select_shop_list(user):
        """
        查询商家列表
        :param user:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 查询营业的所有商家
        db.execute("select * from shop where status = %s", 0)
        shop_res = db.fetchall()
        # 查询用户地址并预处理
        db.execute("select * from user_address where user_id = %s", user.id)
        user_location = db.fetchone()['address_location']
        y1 = user_location.split(',')[0]
        y2 = user_location.split(',')[1]
        shop_addr_list = []
        # 循环所有满足条件的商家
        for i in shop_res:
            x1 = i['address_location'].split(',')[0]
            x2 = i['address_location'].split(',')[1]
            distance = Job.distance_haversine_simple(y1, y2, x1, x2)
            if distance > 10000:
                continue
            else:
                # new一个shop对象并存值
                shop = Shop(address_text=i['address_text'], address_location=i['address_location'], name=i['name'],
                            create_time=i['create_time'], status=i['status'])
                shop_addr_list.append(shop)
        return shop_addr_list
