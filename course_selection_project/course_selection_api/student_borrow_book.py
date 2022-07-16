# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class StudentBorrowBook(object):
    def __init__(self, id=None, book_id =None, user_id=None, status=0, create_time=Job.get_time(),update_time=''):
        """
        学生消费类
        :param id:
        :param book_id:学生卡id
        :param user_id:图书类id
        :param create_time:借书时间
        :param update_time:还书时间
        :param status:0借阅 1已还
        """
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.status = status
        self.create_time = create_time
        self.update_time = update_time