# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.email_utils import SendEmail


class OrderService(object):
    @staticmethod
    def insert_order(order):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute(
            "insert into `order`(order_price,courier_id,user_location,shop_location,distance,start_delivery_time,courier_email) values(%s,%s,%s,%s,%s,%s,%s)",
            (order.order_price, order.courier_id, order.user_location, order.shop_location,
             order.distance, order.start_delivery_time, order.courier_email))
        connection.commit()

