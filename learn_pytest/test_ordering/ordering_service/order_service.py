# -*- coding: utf-8 -*-
import pymysql

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_pymysql.test_api.redis import RedisClient
from learn_project.my_project.test_api.test_public import Job
from learn_pytest.test_ordering.ordering_service.customer_service import CustomerService


class OrderService(object):
    @staticmethod
    def create_order(token, shop_id, amount):
        """
        创建订单（token, shop_id, amount)
        :param token:
        :param shop_id:
        :param amount:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        user_name = RedisClient.create_redis_client().get('user_login' + str(token))
        db.execute("select * from customer_review_user where name = %s", user_name)
        customer = db.fetchone()
        if customer is None:
            print("用户不存在")
        else:
            db.execute("select * from shop_review where id = %s", shop_id)
            shop = db.fetchone()
            if shop is None:
                print("商家不存在")
            else:
                # 店铺营业
                if shop['status'] == 1:
                    print("店铺未营业")
                else:
                    # 插入数据
                    db.execute(
                        "insert into review_order(status, user_id, shop_id, amount, create_time) values (%s,%s,%s,%s,%s)",
                        (0, customer['id'], shop_id, amount, Job.get_time()))
                    connection.commit()
                    # 调用顾客服务类的充值/消费函数，扣除费用
                    CustomerService.charge(amount=amount, token=token, type=1)

    @staticmethod
    def completed_order(order_id):
        """
        完成订单（订单id)
        :param order_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # status 0 下单 1 完成
        db.execute("update review_order set status=%s where id=%s", (1, order_id))
        connection.commit()
        print("订单完成啦")

    @staticmethod
    def review_order(order_id, content, shop_score):
        """
        评论订单（订单id, 评论内容，shop_score)
        :param order_id:
        :param content:
        :param shop_score:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # status 0 下单 1 完成
        db.execute("select * from review_order where id = %s", order_id)
        order_res = db.fetchone()
        if order_res['status'] != 1:
            print("订单未完成")
        else:
            # 创建评论表
            db.execute(
                "insert into learn_database.review(shop_id, user_id, content, status, shop_score, order_id, is_delete, create_time) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                (order_res['shop_id'], order_res['user_id'], content, 0, shop_score, order_id, 0, Job.get_time()))
            connection.commit()
            # 创建评论审核
            db.execute("select * from review where order_id=%s", order_id)
            review_id = db.fetchone()['id']
            db.execute(
                "insert into audit_review(review_id, status, operator_id, is_delete, create_time) values (%s,%s,%s,%s,%s)",
                (review_id, 0, order_res['user_id'], 0, Job.get_time()))
            connection.commit()

    @staticmethod
    def update_review(review_id, new_content):
        """
        修改评论（评论id, 新的评论内容）
        :param review_id:
        :param new_content:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 修改评论表
        db.execute("update learn_database.review set update_content=%s,status=%s where id = %s",
                   (new_content, 0, review_id))
        connection.commit()
        # 修改评论审核记录也修改为未审核
        db.execute(
            "update audit_review set status=%s where id = %s", (0, review_id))
        connection.commit()

    @staticmethod
    def delete_review(review_id):
        """
        删除评论（评论id)
        :param review_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_review where review_id = %s", review_id)
        audit_res = db.fetchone()
        # status 0待审核 1 审核通过 2审核失败
        if audit_res is None:
            print("审核无数据")
        # elif audit_res['status'] != 0:
        #     print("不是待审核的状态哦")
        else:
            # is_delete 0 未删除 1 删除
            # 将评论表的数据软删除 （修改is_delete下同)
            db.execute("update learn_database.review set is_delete=%s where id = %s",
                       (1, review_id))
            connection.commit()
            # 将审核表的数据软删除（如果存在未审核的评论数据的话）
            db.execute("update audit_review set is_delete=%s where review_id = %s",
                       (1, review_id))
            connection.commit()
