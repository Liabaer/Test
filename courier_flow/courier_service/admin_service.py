# -*- coding: utf-8 -*-
import pymysql

from courier_flow.courier_service.vaild_check import ValidCheckUtils
from mysql_pro.test_api.mysql_api import MysqlClient


class AdminService(object):
    @staticmethod
    def register_admin(admin):
        """
        注册管理员
        :param admin:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        if not ValidCheckUtils.check_phone(admin.phone_number):
            print("手机号不合法")
        else:
            #  判断name是否只包含英文名，如果包含其他字符，则过滤，过滤完字符串不允许为空
            if ValidCheckUtils.is_en(admin.name):
                db.execute(
                    "insert into admin_audit(name, phone_number, password,role) values (%s,%s,%s,%s)",
                    (admin.name, admin.phone_number, admin.password, admin.role))
                connection.commit()
            else:
                str = ''
                for i in admin.name:
                    if i.isalpha() is False:
                        continue
                    else:
                        str += i
                if str == '':
                    print("name不合法")
                else:
                    db.execute(
                        "insert into admin_audit(name, phone_number, password,role) values (%s,%s,%s,%s)",
                        (admin.name, admin.phone_number, admin.password, admin.role))
                    connection.commit()