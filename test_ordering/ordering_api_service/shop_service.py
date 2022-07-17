# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from test_ordering.ordering_api_service.vaild_check import ValidCheckUtils


class ShopService(object):
    @staticmethod
    def create_shop(shop):
        """
        创建商家
        :param shop:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 1. 密码必须包含数字和字母，长度为8-15位，提示密码不合法
        if not (ValidCheckUtils.is_en_num(shop.password) and ValidCheckUtils.is_between(shop.password, 8, 15)):
            print("密码不合法")
        else:
            # 2. 商家名必须唯一，如果存在则提示商家名存在，返回false
            db.execute("select * from shop_review where name=%s", shop.name)
            if db.fetchone() is not None:
                print("商家已存在")
                return False
            else:
                # 3. 满足以上条件插入商家表数据
                db.execute(
                    "insert into shop_review(name, password, status, review_score_avg, review_count) values (%s,%s,%s,%s,%s)",
                    (shop.name, shop.name, shop.status, shop.review_score_avg, shop.review_count))
                connection.commit()


    @staticmethod
    def get_score(shop_id):
        """
        获取商家评分（入参商家id)
        :param shop_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from shop_review where id=%s", shop_id)
        shop_res = db.fetchone()
        return round(shop_res['review_score_avg'], 2)

    @staticmethod
    def update_business(shop_id,status):
        """
        修改商家表的status数据为传入的status，控制营业
        :param shop_id:
        :param status:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from shop_review where id=%s", shop_id)
        shop_res = db.fetchone()
        if shop_res['status'] == status:
            print("无需修改")
        else:
            db.execute("update shop_review set status=%s where id=%s",(status,shop_id))
            connection.commit()
            print("修改状态成功")

