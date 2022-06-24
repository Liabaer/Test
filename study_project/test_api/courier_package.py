# -*- coding: utf-8 -*-
import random


class CourierPackage(object):
    def __init__(self, package_name='', package_param={}):
        """
        私有属性
        :param package_id:标签id 初始化函数 id首位随机a-z英文，后四位随机4位数字，标签名和配置参数为入参
        :param package_name:标签名
        :param package_pram:字典 key是车型value是车型对应的背包
        """
        self.package = chr(random.randint(ord('a'), ord('z')))
        for i in range(4):
            self.package += str(random.randint(0,9))
        self.package_name = package_name
        self.package_param = package_param

    def update_package_param(self, new_param):
        """
        修改配置参数函数
        :param new_param:
        :return:
        """
        self.package_pram = new_param
        return self.package_pram

    def update_package_name(self, new_name):
        """
        修改背包名
        :param new_name:
        :return:
        """
        self.package_name = new_name
        return self.package_name

