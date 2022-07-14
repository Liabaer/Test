# -*- coding: utf-8 -*-
import random

import pymysql

from course_selection_project.course_selection_api.school_user import SchoolUser
from mysql_pro.test_api.job_csv import ReadCsv
from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job



class SchoolUserService(object):
    @staticmethod
    def user_login(schoolUser):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from school_user where id=%s", schoolUser.id)
        temp = db.fetchone()
        if temp is None:
            print("用户不存在")
            return False
        else:
            if temp['name'] == schoolUser.name and temp['password'] == schoolUser.password:
                print("登陆成功")
                s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "
                token = ''
                for i in range(14):
                    token += random.choice(s)
                RedisClient.create_redis_client().set("user_login_" + token, temp['id'], ex=86400)
                return token
            else:
                print("姓名或者密码错误")

    @staticmethod
    def user_register(url='user_register.csv'):
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        res = ReadCsv.read_csv(url)
        for i in res:
            user = SchoolUser(name=i[0], password=i[1], type=i[2])
            db.execute("insert into school_user(name,password,type,create_time) values (%s,%s,%s,%s)", (user.name,user.password,user.type,Job.get_time()))
            connection.commit()



