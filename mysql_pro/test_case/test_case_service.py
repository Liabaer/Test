# -*- coding: utf-8 -*-
import csv

import pymysql.cursors

from mysql_pro.test_api.job_csv import ReadCsv
from mysql_pro.test_api.order_service import OrderService
from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_Courier import MySQLCourier
from mysql_pro.test_api.courier_service import CourierService
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.shop_service import ShopService
from mysql_pro.test_api.user_service import UserService
from mysql_pro.test_api.user import User
from mysql_pro.test_api.shop import Shop


class TestCaseService(object):
    @staticmethod
    def generate_order(url='create_order.csv'):
        res = ReadCsv.read_csv(url)
        for i in res:

            order = MysqlOrder(user_email=i[0], user_location=i[1], shop_location=i[2], order_price=i[3],
                               assign_type=i[4])
            OrderService.insert_order(order)

    @staticmethod
    def generate_courier(url='register_courier.csv'):
        res = ReadCsv.read_csv(url)
        for i in res:
            courier = MySQLCourier(courier_email=i[0], delivery_type=i[1], courier_location=i[2])
            CourierService.register_courier(courier)

    @staticmethod
    def update_order_info(url='update_order_status.csv'):
        res = ReadCsv.read_csv(url)
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        for i in res:
            db.execute("update `order` set status =%s where id=%s", (i[1],i[0]))
            connection.commit()

    @staticmethod
    def generate_user(url='create_user.csv'):
        res = ReadCsv.read_csv(url)
        for i in res:
            user = User(name=i[0], email=i[1], phone_number=i[2], password=i[3], amount=i[4])
            UserService.register_user(user)

    @staticmethod
    def generate_shop(url='create_shop.csv', token=''):
        res = ReadCsv.read_csv(url)
        for i in res:
            shop = Shop(name=i[0], address_text=i[1], address_location=i[2])
            ShopService.create_shop(shop, token)