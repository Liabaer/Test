# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class Admin(object):
    def __init__(self, id=None, name='', password='', rule=0, create_time=Job.get_time()):
        # 管理员
        #  1. id
        # 2. name
        # 3. password
        # 4. create_time
        # 5. rule 0 无权限 2评论审核员 3 admin权限
        self.id = id
        self.name = name
        self.password = password
        self.rule = rule
        self.create_time = create_time
