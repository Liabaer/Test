# -*- coding: utf-8 -*-
import pymysql

from accepted_order.service.vaild_check import ValidCheckUtils
from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.test_public import Job


class CourierService(object):
    @staticmethod
    def register_courier(name, password):
        """
        注册
        :param
        :return:
        """
        # 1. name
        # 1. 长度为5-8
        # 2. 并且只能包含大写字母，如果有小写字母，转换为大写
        # 3. 去除元音字母，比如原始姓名为tutu则新名为tt
        # 4. 去除元音之后，检测名字是否为空
        # 5. 在名字前加入yx-的前缀，即yx-tt
        if not ValidCheckUtils.is_between(name, 5, 8):
            print("name长度不符合")
        elif not (ValidCheckUtils.to_lower_case_letters(name)):
            print("name不合法")
        else:
            new_name = ValidCheckUtils.replace_Location(name)
            if new_name == '':
                print("name为空")
            else:
                new_name = "yx-"+ new_name
            # 2. 密码
            # 1. 长度在5-10之间
            # 2. 必须有小写字母
            # 3. 必须有数字

            if not ValidCheckUtils.is_between(password, 5, 10):
                print("password长度不符合")
            elif not (ValidCheckUtils.is_have_lower(password)):
                print("password不含字母")
            elif not (ValidCheckUtils.is_have_num(password)):
                print("password不含数字")
            else:
                connection = MysqlClient.get_connection()
                db = connection.cursor(pymysql.cursors.DictCursor)
                # 3. 写入骑手表
                db.execute("insert into courier_new(name, password, create_time) values (%s,%s,%s)",
                           (new_name, password, Job.get_time()))
                connection.commit()