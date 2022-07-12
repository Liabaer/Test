# -*- coding: utf-8 -*-
class ValidCheckUtils(object):
    @staticmethod
    def is_en(s):
        for i in s:
            if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
                return True
            else:
                return False

    @staticmethod
    def is_num(s):
        for i in s:
            if ord('0') <= ord(i) <= ord('1'):
                return True
            else:
                return False

    @staticmethod
    def is_en_num(s):
        flag1 = False
        flag2 = False
        for x in s:
            # 判断是否为纯数字
            if x.isdigit():
                flag1 = True
            # 判断是否为纯字母
            elif x.isalpha():
                flag2 = True
            else:
                return False
        if flag1 and flag2:
            return True
        return False

    @staticmethod
    def is_between(s, min_len, max_len):
        for i in s:
            if min_len <= len(i) <= max_len:
                return True
            else:
                return False
