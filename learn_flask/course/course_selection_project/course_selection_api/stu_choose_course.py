# -*- coding: utf-8 -*-
class StuChooseCourse(object):
    def __init__(self, id=None, user_id=None, class_id=None, create_time='', status=0):
        """
        学生选课类
        :param id:
        :param user_id: 用户id
        :param class_id:课程id
        :param create_time:创建时间
        :param status : 1取消 0 正常
        """
        self.id = id
        self.user_id = user_id
        self.class_id = class_id
        self.create_time = create_time
        self.status = status
