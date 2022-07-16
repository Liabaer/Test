# -*- coding: utf-8 -*-
import pymysql

from mysql_pro.test_api.mysql_api import MysqlClient
from mysql_pro.test_api.redis import RedisClient
class BookService(object):
    @staticmethod
    def create_book_category(book_category):
        """
        创建图书分类
        :param book_category:（入参 图书分类对象）
        :return:
        """
        connection = MysqlClient.get_connection()
        db=connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from book_category where name=%s", book_category.name)
        if db.fetchone() is not None:
            print("该分类已经存在")
            return False
        else:
            # 将数据写入到图书分类表中
            db.execute("insert into book_category(name, count, create_time) values (%s,%s,%s)", (book_category.name,book_category.count,book_category.create_time))
            connection.commit()
            return True


    @staticmethod
    def create_book(book):
        """
        创建图书
        :param book:（入参图书对象）
        :return:
        """
        connection = MysqlClient.get_connection()
        db = connection.cursor(pymysql.cursors.DictCursor)
        db.execute("select * from book where book_category_id=%s", book.book_category)
        if db.fetchone() is not None:
            print("该分类名已经存在")
            return False
        else:
            # 数据写入到图书表中
            db.execute("insert into book(name, count, new_count, book_category_id, create_time) values (%s,$s,%s,%s,%s)",
                       (book.name, book.count, 0, book.book_category, book.create_time))
            connection.commit()
            db.execute("select * from book_category where name=%s", book.book_category)
            category_old = db.fetchone()['count']
            # 更新图书分类表中count字段
            db.execute("update book_category set count=%s where id=%s", (category_old+1, book.book_category))
            connection.commit()
            return True

