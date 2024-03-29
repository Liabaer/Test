# -*- coding: utf-8 -*-
class Course(object):
    def __init__(self, id=None, name='', teach_id=None, count=None, start_time='', end_time='', create_time=''):
        """
        课程
        :param id:
        :param name: 课程名
        :param teach_id: 教师id
        :param count: 名额总数
        :param new_count: 当前报名人数
        :param start_time: 开始选课时间
        :param end_time: 结束选课时间
        :param create_time: 创建时间
        """
        self.id = id
        self.name = name
        self.teach_id = teach_id
        self.count = count
        self.new_count = 0
        self.start_time = start_time
        self.end_time = end_time
        self.create_time = create_time
