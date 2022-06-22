# -*- coding: utf-8 -*-
class ShopTag(object):

    def __int__(self, Shop_tag_id='', Shop_tag_name=''):
        """
        私有属性
        :param courier_tag_id:标签id
        :param courier_tag_name:标签名
        :return:
        """
        self.Shop_tag_id = Shop_tag_id
        self.Shop_tag_name = Shop_tag_name

    def update_shop_tag_name(self, newname):
        """
        修改标签名
        :param newname:
        :return:
        """
        self.shop_tag_name = newname
        return self.shop_tag_name
