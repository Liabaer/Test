# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText


class SendEmail(object):
    send_email = ''
    send_email_pwd = ''

    @staticmethod
    def send_msg_email(send_name='', send_email='', title='', note=''):
        """
        发送邮件
        :param send_name:收件人姓名
        :param send_email:收件人邮箱
        :param title:标题
        :param note:正文
        :return:
        """
        # 发送邮件整理原理
        # 首先登录发件邮件，然后使用邮件中转站进行转发邮件
        # 具体流程如下
        # 创建发邮件的邮箱（我创建的公共邮箱，不用怕上传）
        send_email = send_email
        # 对应的密码（这个不是登录密码，如果发件的是google email的话就要去配置这个密码）
        send_email_password = 'yblisleuedhnqmwo'
        # 收件人列表
        receive_email_list = ['RenaTuT0401@gmail.com']
        # 创建邮件的内容
        msg = MIMEText("我是邮件的正文123", 'plain', _charset="utf-8")
        msg['from'] = 'tl'  # 这个key自定义发件人姓名
        msg['to'] = 'yanxu'  # 这个key自定义制件人姓名
        msg['subject'] = '我是标题标题'  # 定制邮件的标题
        # 这里我们使用的是google的发邮件的中转站服务（相当于我们电脑投递到他这里，他再投递到其他邮件）
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # 登录发送邮件
        server.login(send_email, send_email_password)
        # 执行发送
        server.sendmail(send_email, receive_email_list, msg.as_string())
        # 发送完毕关闭服务
        server.quit()


SendEmail.send_msg_email(send_name='liabaer', send_email='tt@advx.xyz', title='这里是标标标题', note='这里是正文正文正文')
