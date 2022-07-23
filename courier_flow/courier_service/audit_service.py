# -*- coding: utf-8 -*-
import pymysql

from courier_flow.courier_model.audit_log import AuditLog
from courier_flow.courier_service.audit_log_service import AuditLogService
from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.test_public import Job


class AuditService(object):
    @staticmethod
    def add_audit(audit):
        """
        新增审核
        :param audit:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("insert into audit_record(courier_id, create_time, status) values(%s,%s,%s) ",
                   (audit.courier_id, audit.create_time, audit.status))
        connection.commit()

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
        """
        同意审核
        :param audit_id:
        :param admin_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_record where id=%s", audit_id)
        res = db.fetchone()
        if res is None:
            print("无该审核记录")
        else:
            # 1. 修改审核表数据
            db.execute("update audit_record set status=%s where id=%s", (1, res['courier_id']))
            connection.commit()
            # 2. 修改骑手表数据
            db.execute("update courier_audit_model set status=%s where id=%s", (1, res['courier_id']))
            connection.commit()

            # 3. 调用审核日志类新增审核日志
            log = AuditLog(audit_id=audit_id, status=0, reject_reason='', create_time=Job.get_time(),
                           admin_id=admin_id)
            AuditLogService.add_log(log)



    @staticmethod
    def reject_audit(audit_id, admin_id, reject_reason):
        """
        拒绝审核
        :param audit_id:
        :param admin_id:
        :param reject_reason:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from audit_record where id=%s", audit_id)
        res = db.fetchone()
        if res is None:
            print("无该审核记录")
        else:
            # 1. 修改审核表数据
            db.execute("update audit_record set status=%s where id=%s", (2, audit_id))
            connection.commit()
            # 2. 修改骑手表数据
            db.execute("update courier_audit_model set status=%s where id=%s", (2, res['courier_id']))
            connection.commit()
            # 3. 调用审核日志类新增审核日志
            log = AuditLog(audit_id=audit_id,status=0,reject_reason=reject_reason,create_time=Job.get_time(),admin_id=admin_id)
            AuditLogService.add_log(log)


