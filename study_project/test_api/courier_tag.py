# -*- coding: utf-8 -*-
class CourierTag(object):

    def __int__(self, courier_tag_id='', courier_tag_name=''):
        """
        私有属性
        :param courier_tag_id:标签id
        :param courier_tag_name:标签名
        :return:
        """
        self.courier_tag_id = courier_tag_id
        self.courier_tag_name = courier_tag_name

    def update_courier_tag_name(self, newname):
        """
        修改标签名
        :param newname:
        :return:
        """
        self.courier_tag_name = newname
        return self.courier_tag_name
