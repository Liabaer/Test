# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient


class AuditService(object):
    @staticmethod
    def get_audit_list():
        """
        获取审核列表
        :return:
        """
        # 1. 查询审核表，返回待审核列表。
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_record where status=%s",0)
        audit_res = db.fetchall()
        audit_dict = {}
        audit_list = []
        for audit in audit_res:
            # （返回数组，数组里面的是字典包含骑手id，审核id）
            audit_dict['courier_id'] = audit['courier_id']
            audit_dict['audit_id'] = audit['id']
            audit_list.append(audit_dict)
        return audit_list

    @staticmethod
    def agree_audit(audit_id,admin_id):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_record where status=%s", 0)
        # 1. 修改审核表数据
        # 2. 修改骑手表数据
        # 3. 调用审核日志类新增审核日志
