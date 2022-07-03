# -*- coding: utf-8 -*-
import csv

import pymysql.cursors

from mysql_pro.test_api.job_csv import ReadCsv
from mysql_pro.test_api.order_service import OrderService
from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_Courier import MySQLCourier
from mysql_pro.test_api.courier_service import CourierService
from mysql_pro.test_api.mysql_api import MysqlClient


class TestCaseService(object):
    @staticmethod
    def generate_order(url='create_order.csv'):
        res = ReadCsv.read_csv(url)
        for i in res:
            order = MysqlOrder(user_email=i[0], user_location=i[1], shop_location=i[2], order_price=i[3],
                               assign_type=i[4])
            OrderService.insert_order(order)

    @staticmethod
    def generate_courier(url='register.csv'):
        res = ReadCsv.read_csv(url)
        for i in res:
            courier = MySQLCourier(courier_email=i[0], delivery_type=i[1], courier_location=i[2])
            CourierService.register_courier(courier)

    @staticmethod
    def update_order_info(url='update_order_status.csv'):
        res = ReadCsv.read_csv(url)
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        for i in res:
            db.execute("update `order` set status =%s where id=%s", (i[0], i[1]))
            connection.commit()
