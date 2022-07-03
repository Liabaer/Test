# -*- coding: utf-8 -*-
import json

import pymysql.cursors
import redis

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.mysql_Courier import MySQLCourier
from study_project.test_api.email_utils import SendEmail
from study_project.test_api.test_public import Job
from mysql_pro.test_api.order_service import OrderService
from mysql_pro.test_api.redis import RedisClient


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
        SendEmail.send_msg_email(receive_name=courier.courier_email.split('@')[0],
                                 receive_email=[courier.courier_email],
                                 title='骑手注册成功', note='于' + courier.create_time + '时间注册成功')

    @staticmethod
    def get_order(courier:MySQLCourier, order_id):
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
        # uncompleted_order = {}
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
                OrderService.accept_order(order_id, courier.id)
                print('接单成功')
                RedisClient.create_redis_client().sadd('courier_uncompleted_order_' + str(courier.id), order_id)
                RedisClient.create_redis_client().expire('courier_uncompleted_order_' + str(courier.id), 3600)

        else:
            print('订单不存在')
        # uncompleted_order_info = json.dumps(uncompleted_order)

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
        db.execute("select * from courier where status = %s", ('online'))
        res = db.fetchall()
        # res 没有limit，所以是个数组，循环这个数组，i是字典
        for i in res:
            # 查出来的都是在线的，所以直接通过字典[key]查出对应的value
            courier_online_list.append(i['id'])
        return courier_online_list

    @staticmethod
    def updata_courier_status(courier_id):
        """
        切换上下线（新增函数 传入骑手id)
        :param courier_id:
        :return:
        """
        # 链接数据库，查询骑手的状态
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("select * from courier where  id = %s", (courier_id))
        res = db.fetchone()
        # courier = {}
        # 修改骑手的状态
        if res['status'] == "online":
            db.execute("update courier set status=%s where id = %s", ('offline', courier_id))
            RedisClient.create_redis_client().srem("courier_online_list",courier_id)
            RedisClient.create_redis_client().srem("courier_cache_data_" + str(courier_id))
        else:
            db.execute("update courier set status=%s where id = %s", ('online', courier_id))
            RedisClient.create_redis_client().sadd("courier_online_list", courier_id)
            RedisClient.create_redis_client().expire("courier_online_list", 86400)

            courier_data = {'id': res['id'], 'courier_email': res['courier_email'], 'create_time': res['create_time'],
                            'delivery_type': res['delivery_type'], 'courier_location': res['courier_location']}
            courier_info = json.dumps(courier_data)
            RedisClient.create_redis_client().set("courier_cache_data_" + str(courier_id), courier_info, ex=86400)

    @staticmethod
    def start_delivery(courier:MySQLCourier, order_id):
        """
        始配送函数
        :param courier:骑手对象
        :param order_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("select courier_id from `order` where  id = %s", (order_id))
        res = db.fetchone()
        if courier.id == res['courier_id']:
            # 调用订单服务类的开始配送的订单方法
            pass

    @staticmethod
    def complete_delivery(courier:MySQLCourier, order_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.Cursor)
        db.execute("select * from `order` where  id = %s", (order_id))
        res = db.fetchall()
        if res['status'] == 'accept' and courier.id == res['courier_id']:
            # 满足上面条件，调用订单的完成函数 4. 将骑手的未完成订单缓存中移除这个订单
            OrderService.complete_order(order_id)
            # 存的是集合，我们就用srem(key,  data)把这data从这个key的集合中移出
            RedisClient.create_redis_client().srem('courier_uncompleted_order_' + str(courier.id), order_id)

    @staticmethod
    def get_courier_online():
        res = RedisClient.create_redis_client().smembers('courier_online_list')
        return ','.join(res)

    @staticmethod
    def get_courier_info(courier_id):
        res = RedisClient.create_redis_client().get("courier_cache_data_" + str(courier_id))
        return ','.join(res)

    @staticmethod
    def get_uncompleted_order(courier:MySQLCourier):
        # smembers获取数据，返回一个set集合
        res = RedisClient.create_redis_client().smembers('courier_uncompleted_order_' + str(courier.id))
        return ','.join(res)
