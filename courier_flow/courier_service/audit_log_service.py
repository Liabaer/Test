# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient


class AuditLogService(object):
    @staticmethod
    def add_log(log):
        """
        写入日志
        :param log:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("insert into audit_log(audit_id, create_time, reject_reason, status,admin_id) values(%s,%s,%s,%s,%s) ",
                   (log.audit_id, log.create_time, log.reject_reason, log.status,log.admin_id))
        connection.commit()
