# -*- coding: utf-8 -*-
import pymysql.cursors

from mysql_pro.test_api.mysql_order import MysqlOrder
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
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
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 把订单对象中的值，插入到t_order表中
        db.execute(
            "insert into `order`(status,order_price,courier_id,user_location,shop_location,distance,delivery_fee,create_time,accepted_time,start_delivery_time,completed_time,user_email,assign_type,user_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (order.order_status, order.order_price, order.courier_id, order.user_location, order.shop_location,
             order.distance, order.delivery_fee, order.create_time, order.accepted_time, order.start_delivery_time,
             order.completed_time, order.user_email, order.assign_type, order.user_id))
        connection.commit()
        # 获取insert语句插入后的主键id
        return db.lastrowid

        # # 下单成功通知用户邮件
        # SendEmail.send_msg_email(receive_name=order.user_email.split('@')[0], receive_email=[order.user_email],
        #                          title='下单成功', note='于' + order.create_time + '时间下单成功')

    @staticmethod
    def accept_order(order_id, courier_id):
        """
        接单 （修改订单表的内容）
        :param order_id:订单id
        :param courier_id:骑手id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 查询订单distance
        db.execute("select distance from `order` where id = %s", order_id)
        res = db.fetchone()
        # 调用方法计算配送费
        fee = Job.get_delivery_fee(distance=res['distance'])
        # 1,状态修改为accepted 2. courier_id修改为接单id 3. 配送费修改为实际配送费 4. 修改接单时间为当前时间
        db.execute("update `order` set status = %s, courier_id=%s, delivery_fee=%s where id = %s",
                   ('accepted', courier_id, fee, order_id))
        connection.commit()

    @staticmethod
    def get_uncompleted_list(courier_id):
        """
        获取骑手未完成订单列表
        :param courier_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
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
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("update `order` set status = %s , completed_time = %s where id = %s",
                   ('completed', Job.get_time(), order_id))
        connection.commit()
        db.execute("select * from `order` where id = %s", order_id)
        res = db.fetchone()
        # 发送邮件
        # SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
        #                          title='订单已经完成', note='于' + res['completed_time'] + '时间已完成')

    @staticmethod
    def cancel_order(order_id):
        """
        撤单方法
        :param order_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from `order` where id = %s", order_id)
        res = db.fetchone()
        # 查询订单信息判断是否已经接单
        if res['status'] not in ('pending', 'completed'):
            # 状态修改为pending  courier_id修改为空 accepted_time 修改为空 start_delivery_time 修改为空
            db.execute(
                "update `order` set status = %s, courier_id = %s, accepted_time = %s, start_delivery_time = %s where id = %s",
                ('pending', None, '', '', order_id))
            connection.commit()
            # 清楚redis
            RedisClient.create_redis_client().srem("courier_uncompleted_"+order_id)
        else:
            print("不满足撤单条件")

        # 发送邮件
        # SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
        #                          title='订单已经撤单', note='于' + Job.get_time() + '撤单成功')

    @staticmethod
    def start_delivery(order_id):
        """
        开始配送
        :param order_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute(
            # 修改订单的状态为delivering  修改start_delivery_time为当前时间
            "update `order` set status = %s, start_delivery_time = %s where id = %s",
            ('delivering', Job.get_time(), order_id))
        connection.commit()
        db.execute("select * from `order` where id = %s", order_id)
        res = db.fetchone()
        # 发送邮件
        # SendEmail.send_msg_email(receive_name=res['user_email'].split('@')[0], receive_email=[res['user_email']],
        #                          title='订单开始配送', note='于' + res['start_delivery_time'] + '开始配送')

    @staticmethod
    def delete_order(order_id, user_id):
        """
        取消订单
        :param order_id:
        :param user_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from `order` where id = %s", order_id)
        res = db.fetchone()
        if res is None:
            print("订单不存在")
        elif res['user_id'] == int(user_id):
            db.execute("update `order` set status = %s where id = %s", ('delete', order_id))
            connection.commit()
            print("订单" + str(order_id) + "取消成功")
        else:
            print("订单不属于该用户")

    @staticmethod
    def order_item(item_dict: dict, order_id, token):
        """
        订单商品关联方法
        :param item_dict: key是商品id,value是购买了多少个这个商品
        :param order_id:
        :param token:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 使用token查缓存 userid是否存在
        user_id = RedisClient.create_redis_client().get("user_login_cache_" + str(token))
        if user_id is None:
            print("用户未登录")
        else:
            for k, v in item_dict.items():
                db.execute("select * from item where id = %s", k)
                k_price = db.fetchone()['price']
                # 循环item_dict,将数据循环插入到订单商品表中.还需要根据商品id将商品的当前价格查出来，插入到订单商品表中
                db.execute(
                    "insert into order_item(item_count,item_id,item_price,order_id,create_time) values(%s,%s,%s,%s,%s)",
                    (v, k, k_price, order_id, Job.get_time()))
                connection.commit()
