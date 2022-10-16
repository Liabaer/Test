# -*- coding: utf-8 -*-
import random

import pymysql

from learn_pymysql.test_api.mysql_api import MysqlClient
from learn_project.my_project.test_api.test_public import Job


class VerificationCodeService(object):
    @staticmethod
    def verification_code(smscode):
        """
        创建验证码
        :param smscode:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        for i in range(6):
            smscode.email_code += random.randint(0, 9)
        smscode.create_time = Job.get_time()
        smscode.status = 0
        db.execute("insert into email_code(email,email_code,status,create_time) values(%s,%s,%s,%s)",
                   (smscode.email, smscode.email_code, smscode.status, smscode.create_time))
        connection.commit()
        # # 发送邮件
        # SendEmail.send_msg_email(receive_name=smscode.email.split('@')[0],
        #                          receive_email=[smscode.email],
        #                          title=smscode.email_type, note='您的验证码为'+str(smscode.email_code))

    @staticmethod
    def use_code(email, email_code):
        """
        使用验证码
        :param email:
        :param email_code:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("update email_code set status=%s,use_time=%s where email_code =%s ", (1, Job.get_time(), email_code))
        connection.commit()

    @staticmethod
    def check_code(email, email_code):
        """
        查询验证码函数
        :param email:
        :param email_code:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from email_code where email_code =%s ", (email_code))
        res = db.fetchone()
        if res is not None and res['status'] != 1:
            return True
        else:
            return False
