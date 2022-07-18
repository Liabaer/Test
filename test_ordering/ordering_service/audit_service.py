# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.test_public import Job


class AuditService(object):
    @staticmethod
    def get_audit_list(type):
        """
        获取审核列表（type)
        :param type:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # type = 0查询所有未审核的审核列表返回数组字典   0待审核 1 审核通过 2审核失败
        # 字典里的key是，商家名，用户id，用户名，评论id,订单id，评论内容（要区分新老评论，只返回最新的
        audit_list = []
        audit_dict = {}
        if type == 0:
            db.execute("select * from audit_review where status=%s", 0)
            audit_res = db.fetchall()
            for audit in audit_res:
                db.execute("select * from learn_database.review where id = %s", audit['review_id'])
                audit_temp = db.fetchone()
                audit_dict["商家名"] = audit_temp['shop_id']
                # ...
                audit_list.append(audit_dict)
        # type = 1查询所有审核通过的审核列表返回数组字典
        # 字典里的key是，商家名，用户id，用户名，评论id,订单id，操作人名称，评论内容（要区分新老评论，只返回最新的））
        elif type == 1:
            db.execute("select * from audit_review where status=%s", 1)
            audit_res = db.fetchall()
            for audit in audit_res:
                pass
        # type = 2查询所有审核拒绝的审核列表
        # 字典里的key是，商家名，用户id，用户名，评论id,订单id，操作人名称，拒绝原因，评论内容（要区分新老评论，只返回最新的)）
        elif type == 2:
            db.execute("select * from audit_review where status=%s", 2)
            audit_res = db.fetchall()
            for audit in audit_res:
                pass
        else:
            print("无效的参数")

    @staticmethod
    def reject_audit(reject_reason, admin_id, review_id):
        """
        拒绝审核
        :param reject_reason:
        :param admin_id:
        :param review_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_review where review_id = %s", review_id)
        res = db.fetchone()
        if res is None:
            print("评论不存在")
        else:
            #  1. 修改审核表的记录  0待审核 1 审核通过 2审核失败
            db.execute("update audit_review set status=%s,reject_reason=%s,operator_id=%s where review_id=%s",
                       (2, reject_reason, admin_id))
            connection.commit()
            #  2. 修改评论表的记录  0 待审核 1 审核 2 拒绝
            db.execute("update review set status=%s,update_time=%s where id=%s",
                       (2, Job.get_time(), review_id))
            connection.commit()

    @staticmethod
    def agree_audit(admin_id, review_id):
        """
        通过审核
        :param admin_id:
        :param review_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_review where review_id = %s", review_id)
        res = db.fetchone()
        if res is None:
            print("评论不存在")
        else:
            #  1. 修改审核表的记录  0待审核 1 审核通过 2审核失败
            db.execute("update audit_review set status=%s,operator_id=%s where review_id=%s",
                       (1, admin_id))
            connection.commit()
            #  2. 修改评论表的记录  0 待审核 1 审核 2 拒绝
            db.execute("update review set status=%s,update_time=%s where id=%s",
                       (1, Job.get_time(), review_id))
            connection.commit()
            # 3. 查询该商家的所有评论通过的数据，求出平均值和评论数，写入商家表
            db.execute(
                "select * from review as r left join shop_review as s on r.shop_id=s.id where r.id=%s and r.status=%s",
                (review_id, 1))
            res = db.fetchall()
            count = 0
            for r in res:
                count += 1
            # 写入商家表
            db.execute("update shop_review set review_score_avg=%s,review_count=%s where id = %s",
                       (1, count, res['shop_id']))
