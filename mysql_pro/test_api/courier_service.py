# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.mysql_Courier import MySQLCourier
from study_project.test_api.email_utils import SendEmail
from study_project.test_api.test_public import Job
from mysql_pro.test_api.order_service import OrderService

class CourierService(object):

    @staticmethod
    def register_courier(courier: MySQLCourier):
        """
        创建新骑手
        :param courier: 骑手对象
        :return:
        """
        connection = MysqlClient.get_connection()
        # 获取数据库操作对象
        db = connection.cursor(pymysql.cursors.Cursor)
        # 把骑手对象中的值，插入到t_courier表中
        db.execute(
            "insert into courier(status,delivery_type,courier_location,create_time,last_online_time,courier_email) values (%s,%s,%s,%s,%s,%s)",
            (courier.status, courier.delivery_type, courier.courier_location,
             courier.create_time, courier.last_online_time, courier.courier_email)),
        # 记得需要commit一下
        connection.commit()

        # 自增长id
        print('注册成功，注册的骑手id：' + str(db.lastrowid))
        # 发送邮件通知骑手注册成功
        SendEmail.send_msg_email(receive_name=courier.courier_email.split('@')[0], receive_email=[courier.courier_email],
                                 title='骑手注册成功', note='于' + courier.create_time + '时间注册成功')

    @staticmethod
    def get_order(courier, order_id):
        """
         接单
        :param courier:骑手对象
        :param order_id:订单id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        # 执行sql 查询数据库表该订单id的数据
        db.execute("select * from `order` where id = %s", (order_id))
        # 获取结果（结果是字典）
        res = db.fetchone()
        # 满足以下条件则接单成功，失败打印具体的失败原因
        if res is not None:
            x = res.get('user_location').split(',')
            y = courier.courier_location.split(',')
            distance = Job.distance_haversine_simple(x[0], x[1], y[0], y[1])
            # 骑手处于online状态
            if courier.status != 'online':
                print('接单失败,骑手未上线')
            # 骑手距离商家距离小于3000米
            elif distance > 3000:
                print('接单失败，骑手距离商家距离大于3000米')
            else:
                # 调用订单接单方法
                OrderService.accept_order(order_id, courier.courier_id)
                print('接单成功')
        else:
            print('订单不存在')

    @staticmethod
    def get_courier_online_list():
        """
        获取在线配送员id列表
        1. 入参无
        2. 查询t_courier表有那些在线配送员
        3. 返回逗号拼接的骑手id列表
        :return:
        """
        courier_online_list = []
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("select * from courier where status = %s",('online'))
        res = db.fetchall()
        # res 没有limit，所以是个数组，循环这个数组，i是字典
        for i in res:
            # 查出来的都是在线的，所以直接通过字典[key]查出对应的value
            courier_online_list.append(i['id'])
        return courier_online_list
