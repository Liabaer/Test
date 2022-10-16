# -*- coding: utf-8 -*-
class ShopTag(object):

    def __int__(self, shop_tag_id='', shop_tag_name=''):
        """
        私有属性
        :param courier_tag_id:标签id
        :param courier_tag_name:标签名
        :return:
        """
        self.shop_tag_id = shop_tag_id
        self.shop_tag_name = shop_tag_name

    def update_shop_tag_name(self, newname):
        """
        修改标签名
        :param newname:
        :return:
        """
        self.shop_tag_name = newname
        return self.shop_tag_name
