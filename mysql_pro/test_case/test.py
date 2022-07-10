# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_api.commodity_service import CommodityService
from mysql_pro.test_api.coupon import Coupon
from mysql_pro.test_api.coupon_service import CouponService
from mysql_pro.test_api.user_service import UserService
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
# AutoService.auto_service()


# new_test
# TestCaseService.generate_user()

# token = UserService.user_login('liabaer','aaa111bbb222c')
# print(token)
UserService.user_recharge(token='y8r0t2f5j9y6a0a0', amount=25)
# UserService.add_user_address(token=token,location='1.30205,103.880356',addr_text='30-Jln-Benaan-Kapal,sg-399631')
# UserService.login_out(token=token)
# TestCaseService.generate_shop(token=token)
# UserService.update_pwd(token=token,pwd='a123b123c123',new_pwd='aaa111bbb222c')

# CommodityService.create_commidity(price=1,count=100,shop_id=1,token='y8r0t2f5j9y6a0a0')
# CommodityService.create_commidity(price=2,count=50,shop_id=1,token='y8r0t2f5j9y6a0a0')
# # CommodityService.add_count(1,50,'y8r0t2f5j9y6a0a0')
# CommodityService.update_price(item_id=1,price=3,token='y8r0t2f5j9y6a0a0')
# CommodityService.update_price(item_id=2,price=4,token='y8r0t2f5j9y6a0a0')
# coupon = Coupon(coupon_price=0, coupon_discount=0.1, type=1)
# CouponService.create_coupon(coupon=coupon, token='y8r0t2f5j9y6a0a0')
# CouponService.send_coupon(coupon_id=2,user_id=1,token='y8r0t2f5j9y6a0a0')

# UserService.place_order(user_addr_id=2, shop_id=1, item_dict={1: 3, 2: 4}, coupon_id=2, token='y8r0t2f5j9y6a0a0')
UserService.delete_order(token='y8r0t2f5j9y6a0a0',order_id=8)