# -*- coding: utf-8 -*-


class Book(object):
    def __init__(self, id=None, book_category=None, now_count=0, name='', count=0,
                 status=0):
        """
        图书
        :param id:
        :param name:分类名（如计算机）
        :param count:该分类下图书的总数
        :param now_count:目前借出的数量
        :param status:0 正常 1 删除
        """
        self.id = id
        self.name = name
        self.book_category = book_category
        self.count = count
        self.now_count = now_count
        self.status = status
