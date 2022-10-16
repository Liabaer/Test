# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class AuditRecord(object):
    def __init__(self, id=None, courier_id=None, status=0, create_time=Job.get_time()):
        """
        审核类
        :param id:
        :param courier_id:
        :param status: 0 未审核 1 审核通过
        :param create_time:
        """
        self.id = id
        self.courier_id = courier_id
        self.status = status
        self.create_time = create_time
