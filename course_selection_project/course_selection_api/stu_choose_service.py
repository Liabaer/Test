# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
from study_project.test_api.test_public import Job
from web_project.web_api.vaild_check import ValidCheckUtils


class StuChooseCls(object):
    @staticmethod
    def create_course(token, course):
        """
        创建课程
        :param token:
        :param course:
        :return:
        """
        # # 判断token是否合法 又不用判断了
        # if not ValidCheckUtils.is_en_num(token):
        #     print("token不合法")
        #     return

        #  start_time不允许大于end_time，end_time不允许小于当前时间
        if course.end_time > course.start_time and course.end_time > Job.get_time():
            connection = MysqlClient.get_connection()
            db = connection.cursor(pymysql.cursors.DictCursor)
            user_id = RedisClient.create_redis_client().get("user_login_" + str(token))
            if user_id is None:
                print('用户未登录')
            else:
                db.execute("select * from school_user where id = %s", user_id)
                res = db.fetchone()
                db.execute("select * from school_user where id = %s", course.teach_id)
                teach_res = db.fetchone()
                # 以及判断token的权限是否为老师
                if res is None:
                    print("用户不存在")
                elif res['type'] == 0:
                    print('非教师登陆')
                # teach_id必须有效（在用户表中存在，并且是type是教师类型）
                elif teach_res is None or teach_res['type'] == 0:
                    print("teach_id不存在或权限错误")
                else:
                    #  录入课程的信息到课程表中
                    db.execute(
                        "insert into school_class(name,teach_id,count,new_count,start_time,end_time,create_time) values (%s,%s,%s,%s,%s,%s,%s)",
                        (course.name, course.teach_id, course.count, 0, course.start_time,
                         course.end_time, Job.get_time()))
                    connection.commit()
        else:
            print("课程时间参数不合法")

    @staticmethod
    def get_course():
        """
        获取课程列表
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from school_class")
        res = db.fetchall()
        course_list = []
        for i in res:
            course_dict = {}
            if i['start_time'] <= Job.get_time() <= i['end_time']:
                for k, v in i.items():
                    if k == 'teach_id':
                        db.execute("select * from school_user where id=%s", v)
                        teach_name = db.fetchone()['name']
                        course_dict['teach_name'] = teach_name
                    else:
                        course_dict[k] = v
            course_list.append(course_dict)
        return course_list

    @staticmethod
    def choose_course(token, course_id):
        """
         选课
        :param token:
        :param course_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        user_id = RedisClient.create_redis_client().get("user_login_" + str(token))
        # 判断token对应的用户是否存在
        if user_id is None:
            print('用户未登录')
            return False
        else:
            db.execute("select * from school_user where id = %s", user_id)
            res = db.fetchone()
            # 判断token对应的用户是否存在
            if res is None:
                print("用户不存在")
                return False
            else:
                # 查询 course_id 的 school_class
                db.execute("select * from school_class where id = %s", course_id)
                cls_res = db.fetchone()
                # 查询course_id 的选课信息
                db.execute("select * from user_class where class_id = %s and user_id=%s", (course_id, user_id))
                user_cls_res = db.fetchone()
                # 判断用户是否选过了这门课
                if user_cls_res is not None:
                    print('用户已经选过该课程')
                    return False
                # 这门课程当前时间还能否选
                elif not (cls_res['start_time'] < Job.get_time() < cls_res['end_time']):
                    print("当前时间该课程不可选")
                    return False
                # 选课人数是否到达上限
                elif cls_res['new_count'] + 1 > cls_res['count']:
                    print("选课人数达上限")
                    return False
                else:
                    # 新增学生选课表
                    db.execute("insert into user_class(user_id, class_id, create_time) values (%s,%s,%s)",
                               (user_id, course_id, Job.get_time()))
                    connection.commit()
                    # 修改课程表数据
                    db.execute("update school_class set new_count=%s where id = %s",
                               (cls_res['new_count'] + 1, course_id))
                    connection.commit()
                    return True
