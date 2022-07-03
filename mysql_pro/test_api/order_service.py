# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.email_utils import SendEmail
from study_project.test_api.test_public import Job


class OrderService(object):
    @staticmethod
    def insert_order(order: MysqlOrder):
        """
        创建订单
        :param order:订单对象
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        # 把订单对象中的值，插入到t_order表中
        db.execute(
            "insert into `order`(status,order_price,courier_id,user_location,shop_location,distance,delivery_fee,create_time,accepted_time,start_delivery_time,completed_time,courier_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (order.order_status, order.order_price, order.courier_id, order.user_location, order.shop_location,
             order.distance, order.delivery_fee, order.create_time, order.accepted_time, order.start_delivery_time,
             order.completed_time, order.user_email))
        connection.commit()

        # 下单成功通知用户邮件
        SendEmail.send_msg_email(receive_name=order.user_email.split('@')[0], receive_email=[order.user_email],
                                 title='下单成功', note='于' + order.create_time + '时间下单成功')

    @staticmethod
    def accept_order(order_id, courier_id):
        """
        接单 （修改订单表的内容）
        :param order_id:订单id
        :param courier_id:骑手id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        # 查询订单distance
        db.execute("select distance from `order` where id = %s", (order_id))
        res = db.fetchone()
        # 调用方法计算配送费
        fee = Job.get_delivery_fee(distance=res['distance'])
        # 1,状态修改为accepted 2. courier_id修改为接单id 3. 配送费修改为实际配送费 4. 修改接单时间为当前时间
        db.execute("update `order` set status = %s, courier_id=%s, delivery_fee=%s where id = %s",
                   ('accepted', order_id, courier_id, fee))

    @staticmethod
    def get_uncompleted_list(courier_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        # 查询t_order表，查询骑手有那些订单未完成
        db.execute("select * from `order` where courier_id = %s and status != %s", (courier_id, 'completed'))
        res = db.fetchall()
        uncompleted_list = []
        for i in res:
            uncompleted_list.append(str(i['id']))
        return ','.join(uncompleted_list)

    @staticmethod
    def complete_order(order_id):
        """
        完成订单
        :param order_id: 订单id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("update `order` set status = %s , completed_time = %s where id = %s",
                   ('completed', Job.get_time(), order_id))
        db.execute("select * from `order` where id = %s", (order_id))
        res = db.fetchone()
        # 发送邮件
        SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
                                 title='订单已经完成', note='于' + res['completed_time'] + '时间已完成')

    @staticmethod
    def cancel_order(order_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("select * from `order` where id = %s", (order_id))
        res = db.fetchone()
        if res['status'] not in('pending','completed'):
            db.execute("update `order` set status = %s, courier_id = %s, accepted_time = %s, start_delivery_time = %s where id = %s",
                    ('pending', '','','', order_id))
        else:
            print("不满足撤单条件")

        # 发送邮件
        SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
                                 title='订单已经撤单', note='于' + Job.get_time() + '撤单成功')

    @staticmethod
    def start_delivery(order_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute(
            "update `order` set status = %s, start_delivery_time = %s where id = %s",
            ('delivering', Job.get_time(), order_id))
        db.execute("select * from `order` where id = %s", (order_id))
        res = db.fetchone()
        # 发送邮件
        SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
                                 title='订单开始配送', note='于' + res['start_delivery_time'] + '开始配送')
