# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.test_public import Job
from test_ordering.ordering_service.vaild_check import ValidCheckUtils


class AdminService(object):
    @staticmethod
    def create_admin(admin):
        """
        创建管理员（管理员对象）
        :param admin:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 1. 密码必须包含数字和字母，长度为8-15位，提示密码不合法
        if not (ValidCheckUtils.is_en_num(admin.password) and ValidCheckUtils.is_between(admin.password, 8, 15)):
            print("密码不合法")
            return False
        else:
            db.execute("select * from learn_database.admin where password=%s", admin.name)
            if db.fetchone() is not None:
                print("管理员已存在")
                return False
            else:
                # rule 0 无权限 2评论审核员 3 admin权限
                db.execute(
                    "insert into learn_database.admin(name, password, rule, create_time) values (%s,%s,%s,%s)",
                    (admin.name,admin.password,admin.rule, Job.get_time()))
                connection.commit()
                return False