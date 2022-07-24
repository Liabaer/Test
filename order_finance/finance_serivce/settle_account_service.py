# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from order_finance.finance_serivce.courier_service import CourierService
from study_project.test_api.test_public import Job


class SettleAccountService(object):
    @staticmethod
    def add_settle_account(order_id, amount):
        """
         新增结算订单
        :param order_id:
        :param amount:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # db.execute("select * from order_finance where id=%s", order_id)
        # courier_id = db.fetchone()['courier_id']
        db.execute("insert into order_finance_settle_account(amount, status, order_id, create_time) values (%s,%s,%s,%s)",
                   (amount, 0, order_id, Job.get_time()))
        connection.commit()

    @staticmethod
    def get_unsettle():
        """
        查询未结算订单
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from order_finance_settle_account where status=%s", 0)
        res = db.fetchall()
        if res is None:
            print("无未结算的订单")
        else:
            order_list = []
            for order in res:
                # print(order)
                order_dict = {'order_id': order['id'], 'amount': order['amount']}
                # print(order_dict)
                order_list.append(order_dict)
            # print(order_list)
            return order_list

    @staticmethod
    def settle_account(order_id, courier_id):
        """
        结算
        :param order_id:
        :param courier_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 更新结算表的courier_id和status字段
        db.execute("update order_finance_settle_account set status=%s,courier_id=%s where order_id=%s", (1, courier_id, order_id))
        connection.commit()
        db.execute("select * from order_finance_settle_account where order_id=%s", order_id)
        amount = db.fetchone()['amount']

        #调用骑手服务类的新增工资方法
        CourierService.add_amount(courier_id,amount)


