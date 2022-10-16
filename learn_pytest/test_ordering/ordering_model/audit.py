# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.test_public import Job


class Audit(object):
    def __init__(self, id=None, review_id=None, status=0, create_time=Job.get_time(), reject_reason='',
                 operator_id=None, is_delete=0):
        # 审核
        # 1. id
        # 2. review_id
        # 3. status 0待审核 1 审核通过 2审核失败
        # 4. create_time
        # 5. reject_reason 拒绝原因
        # 6. operator_id 操作人id
        # 7. is_delete 0正常 1删除
        self.id = id
        self.review_id = review_id
        self.status = status
        self.create_time = create_time
        self.reject_reason = reject_reason
        self.operator_id = operator_id
        self.is_delete = is_delete
