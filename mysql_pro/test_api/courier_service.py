# -*- coding: utf-8 -*-
from mysql_pro.test_api.mysql_api import MysqlClient
from  mysql_pro.test_api.mysql_Courier import MySQLCourier

class CourierService(object):
    @staticmethod
    def register_courier(courier):
        courier = MySQLCourier()

        MysqlClient.db.execute("insert into courier(id) values (%s,%s,%s,%s,%s,%s,%s)",
                               (courier.id,courier.status,courier.delivery_type,courier.courier_location,
                                courier.create_time,courier.last_online_time,courier.courier_email))

        print('注册成功，注册的骑手id：'+str(courier.courier_id))



