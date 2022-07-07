# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job


class ShopService(object):
    @staticmethod
    def create_shop(shop,token):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if token is None:
            print("用户未登录")
        else:
            s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
            user_id = RedisClient.create_redis_client().delete("user_login_cache_" + str(token))
            db.execute("select * from user where id = %s", (user_id))
            res = db.fetchone()
            if res['type'] != 'admin':
                print("权限不足")
            elif (for i in shop.name if i not in s):
                print("商家名称不合法")
            elif len(shop.address_text) < 10:
                print("商家地址文本太短")
            else:
                location = str(round(int(shop.address_location),6))
                db.execute("insert into shop(name,address_text,address_location,create_time) values (%s,%s,%s,%s)",
                           (shop.name,shop.address_text,location,Job.get_time()))
                connection.commit()

    @staticmethod
    def select_shop_list(user):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from shop where status = %s", ('0'))
        shop_res = db.fetchall()
        db.execute("select * from user_address where id = %s", (user.id))
        user_location = db.fetchone()['address_location']
        y1 = user_location.split(',')[0]
        y2 = user_location.split(',')[1]
        shop_addr_list = []
        for i in shop_res:
            x1 = i['address_location'].split(',')[0]
            x2 = i['address_location'].split(',')[1]
            distance = Job.distance_haversine_simple(y1,y2,x1,x2)
            if distance > 10000:
                continue
            else:
                # 我知道题目是对象，不知道怎么存，先存个id吧
                shop_addr_list.append(i['id'])
        return shop_addr_list


