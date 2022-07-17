# -*- coding: utf-8 -*-
class Customer(object):
    def __init__(self,id=None,amount=0,name='',password='',create_time=''):
        """
        顾客
        :param id:
        :param amount:
        :param name:
        :param password:
        :param create_time:
        """
        self.id = id
        self.amount = amount
        self.name = name
        self.password = password
        self.create_time = create_time