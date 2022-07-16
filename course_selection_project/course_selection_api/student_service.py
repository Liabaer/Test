# -*- coding: utf-8 -*-
from datetime import datetime

import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from study_project.test_api.test_public import Job


class StudentService(object):
    @staticmethod
    def create_card(student_card):
        """
        申请学生卡
        :param student_card: （入参 学生卡对象）
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        # 将数据写入到卡分类表中
        db.execute("insert into student_card(name, amount, create_time) values (%s,%s,%s)",
                   (student_card.name, student_card.amount, Job.get_time()))
        connection.commit()
        return True

    @staticmethod
    def use_card(type, amount, card_id):
        """
        使用学生卡
        :param type:
        :param amount:
        :param card_id:
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from student_card where id = %s", card_id)
        old = db.fetchone()
        # 消费
        if type == 0 and old['amount'] < amount:
            print("余额不足")
        elif type == 0 and old['amount'] >= amount:
            db.execute("update student_card set amount=%s where id=%s", (old['amount'] - amount, card_id))
            connection.commit()
            print("消费成功")
            #  将充值金额或者消费金额写入到学生消费表中
            db.execute("insert into student_consumer_log(amount, type, create_time) values (%s,%s,%s)",
                       (amount, type, Job.get_time()))
            connection.commit()
        #  充值
        elif type == 1:
            db.execute("update student_card set amount=%s where id=%s", (old['amount'] + amount, card_id))
            connection.commit()
            print("充值成功")
            #  将充值金额或者消费金额写入到学生消费表中
            db.execute("insert into student_consumer_log(amount, type, create_time) values (%s,%s,%s)",
                       (amount, type, Job.get_time()))
            connection.commit()
        else:
            print("未知的参数")

    @staticmethod
    def borrow_book(book_id, card_id):
        """
        借阅
        :param book_id:入参图书id
        :param card_id:学生卡id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from student_card where id = %s", card_id)
        card_res = db.fetchone()
        if card_res is None:
            print("学生卡不存在")
        else:
            db.execute("select * from book where id = %s", book_id)
            book_res = db.fetchone()
            if book_res is None:
                print("图书不存在")
            else:
                if book_res['now_count'] >= book_res['count']:
                    print("库存不足")
                else:
                    db.execute(
                        "insert into student_borrow_book(user_id, book_id, status, create_time) values (%s,%s,%s,%s)",
                        (card_id, book_id, 0, Job.get_time()))
                    connection.commit()
                    db.execute("update book set now_count=%s where id=%s", (book_res['now_count'] + 1, book_id))
                    connection.commit()
                    print("借阅成功")

    @staticmethod
    def return_book(book_id, card_id):
        """
        还书
        :param book_id:入参图书id
        :param card_id:学生卡id
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from student_card where id = %s", card_id)
        card_res = db.fetchone()
        if card_res is None:
            print("学生卡不存在")
        else:
            db.execute("select * from book where id = %s", book_id)
            book_res = db.fetchone()
            if book_res is None:
                print("图书不存在")
            else:
                if book_res['now_count'] >= book_res['count']:
                    print("库存不足")
                else:
                    #  修改学生借书表的数据
                    db.execute(
                        "update student_borrow_book set status=%s,update_time=%s where book_id=%s and user_id=%s",
                        (1, Job.get_time(), book_id, card_id))
                    connection.commit()
                    #  修改图书表的借出字段
                    db.execute("update book set now_count=%s where id=%s", (book_res['now_count'] - 1, book_id))
                    connection.commit()
                    print("还书成功")
                    # 根据还书时间计算消费金额（一本书一天按照5毛计算，不足一天按一天）

                    db.execute("select * from student_borrow_book where book_id=%s and user_id=%s", (book_id, card_id))
                    borrow_res = db.fetchone()
                    # total_seconds 计算2个时间相差了多少秒
                    time = (datetime.strptime(borrow_res['update_time'], '%Y.%m.%d %H:%M:%S') - datetime.strptime(
                        borrow_res['create_time'], '%Y.%m.%d %H:%M:%S')).total_seconds()
                    if (time % 3600 * 24) != 0:
                        amount = (int(time / 3600 * 24) + 1) * 0.5
                    else:
                        amount = int(time / 3600 * 24) * 0.5
                    # 调用使用学生卡函数
                    StudentService.use_card(0, amount, card_id)
