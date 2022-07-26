# -*- coding: utf-8 -*-
import random
from datetime import datetime


class ValidCheckUtils(object):
    @staticmethod
    def is_en(s):
        flag = False
        for i in s:
            if ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
                flag = True
            else:
                return False
        if flag:
            return True

    @staticmethod
    def is_num(s):
        flag = False
        for i in str(s):
            if ord('0') <= ord(i) <= ord('9'):
                flag = True
            else:
                return False
        if flag:
            return True

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
        if (flag1 == True and flag2 == True) or '_' in s:
            return True
        return False

    @staticmethod
    def is_between(s, min_len, max_len):
        if min_len <= len(str(s)) <= max_len:
            return True
        else:
            return False

    @staticmethod
    def check_phone(s):
        if s[0] == 0 and len(s) == 9:
            return True
        elif len(s) == 8:
            return True
        else:
            return False

    @staticmethod
    def become_token():
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_ "
        token = ''
        for i in range(14):
            token += random.choice(s)
        return token

    @staticmethod
    def to_lower_case_letters(s):
        if not s.isalpha():
            return False
        else:
            res = s.lower()
            return res

    @staticmethod
    def to_upper_case_letters(s):
        if not s.isalpha():
            return False
        else:
            res = s.upper()
            return res

    @staticmethod
    def change_Location(s):
        start = ''
        end = ''
        temp = ['a', 'e', 'i', 'o', 'u']
        for i in s:
            if i in temp:
                start += i
            else:
                end += i
        return start + end

    @staticmethod
    def replace_Location(s):
        new_s = ''
        temp = ['A', 'E', 'I', 'O', 'U']
        for i in s:
            if i in temp:
                continue
            else:
                new_s += i
        return new_s

    @staticmethod
    def is_have_lower(s):
        for i in s:
            if ord('a') <= ord(i) <= ord('z'):
                return True
            else:
                return False


    @staticmethod
    def is_have_num(s):
        for i in s:
            if ord('0') <= ord(i) <= ord('9'):
                return True
            else:
                return False

    @staticmethod
    def time_diff(t1, t2):
        time = (datetime.strptime(t1, '%Y.%m.%d %H:%M:%S') - datetime.strptime(
                    t2, '%Y.%m.%d %H:%M:%S')).total_seconds()
        return time
