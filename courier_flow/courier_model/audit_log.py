# -*- coding: utf-8 -*-
from study_project.test_api.test_public import Job


class AuditLog(object):
    def __init__(self, id=None, audit_id=None, status=0, reject_reason='', create_time=Job.get_time()):
        """
        审核日志类
        :param id:
        :param audit_id:
        :param status:0 通过 1 未通过
        :param reject_reason: 失败原因
        :param create_time:
        """
        self.id = id
        self.audit_id = audit_id
        self.status = status
        self.reject_reason = reject_reason
        self.create_time = create_time
