# -*- coding: utf-8 -*-

class Setting(object):
    @staticmethod
    def set_hd():
        hd = {'language': 'cn', 'device': 'tt-test', 'Content-Type': 'application/json'}
        return hd

    # pwd = {'email':'Rena0401@gmail.com','password':'34dfsdAf324sf2@s'}
    @staticmethod
    def set_url():
        base_url = 'http://localhost:10001'
        return base_url
