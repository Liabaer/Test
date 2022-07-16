# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class BookCategory(object):
    def __init__(self, id=None, name='', count=0, create_time=Job.get_time(), status=0):
        """
        图书分类表
        :param id:
        :param name:分类名（如计算机）
        :param count:该图书的总数
        :param create_time:
        :param status:0 正常 1 删除
        """
        self.id = id
        self.name = name
        self.count = count
        self.create_time = create_time
        self.status = status
