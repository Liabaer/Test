# -*- coding: utf-8 -*-
import pymysql


class MysqlClient(object):
    host = '127.9.0.1'
    port = 3306
    user = 'root'
    password = ''
    db = 'learn_db'

    @staticmethod
    def get_connection():
        return pymysql.connect(host=MysqlClient.host,port=MysqlClient.port,user=MysqlClient.user,password=MysqlClient.password,db=MysqlClient.db)