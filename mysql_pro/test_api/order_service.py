# -*- coding: utf-8 -*-
from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_api import MysqlClient

class OrderService(object):
    @staticmethod
    def insert_order(order):
        order = MysqlOrder()
        MysqlClient.db.execute("insert into order(id) values()",
                               (order.id,order.order_price, order.courier_id, order.user_location, order.shop_location,
                                order.distance, order.start_delivery_time, order.courier_email))
