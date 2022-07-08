# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_case.test_case_service import TestCaseService
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_Courier import MySQLCourier
from mysql_pro.test_api.courier_service import CourierService
from mysql_pro.test_api.order_service import OrderService
from mysql_pro.test_api.auto_service import AutoService

# 调用下单
# TestCaseService.generate_order()

# 调用注册骑手
# TestCaseService.generate_courier()

# connection = MysqlClient.get_connection()
# db = connection.cursor(pymysql.cursors.DictCursor)
# # db.execute("select * from `order` where id = %s", (1))
# # order_res = db.fetchone()
# db.execute("select * from courier where id in(%s,%s)", (1,2))
# courier_res = db.fetchall()
# for i in courier_res:
#     courier = MySQLCourier(id=i['id'], courier_location=i['courier_location'],
#                            status=i['status'])
#     CourierService.update_courier_status(courier.id)
#
# order = MysqlOrder(id=order_res['id'])

#
# db.execute("select * from courier where id = %s", (1))
# courier1_res = db.fetchone()
# courier1 = MySQLCourier(id=courier1_res['id'], courier_location=courier1_res['courier_location'],status=courier1_res['status'])

# CourierService.get_order(courier, order.id)
# CourierService.start_delivery(courier,order.id)
# CourierService.complete_delivery(courier,order.id)


# 调用修改文件
# TestCaseService.update_order_info()
# OrderService.cancel_order(1)
AutoService.auto_service()