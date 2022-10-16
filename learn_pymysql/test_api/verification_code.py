# -*- coding: utf-8 -*-
class VerificationCode(object):
    def __init__(self, id=None, email='', email_code=0, status=0, create_time='', email_type='update_password',
                 user_time=''):
        """
        :param id:
        :param email:
        :param email_code:
        :param status:0表示已发送 1表示已使用
        :param create_time:发送验证码的时间
        :param email_type:验证码类型 update_password/update_email
        :param user_time:使用时间
        """
        self.id = id
        self.email = email
        self.email_code = email_code
        self.status = status
        self.create_time = create_time
        self.email_type = email_type
        self.user_time = user_time
