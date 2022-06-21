# -*- coding: utf-8 -*-
import math
import datetime

class Job(object):

    @staticmethod
    def distance_haversine_simple(lat1, lng1, lat2, lng2):
        """
        计算2个经纬度之间的直线距离（输入2个经纬度 输出距离） 参考下方代码计算
        计算经纬度直线距离 （后面考虑多项式优化版本）
        :param lng1:
        :param lat2:
        :param lng2:
        :return:直线距离
        """
        dx = lng1 - lng2
        dy = lat1 - lat2
        b = (lat1 + lat2) / 2.0
        lx = math.radians(dx) * 6367000.0 * math.cos(math.radians(b))
        ly = 6367000.0 * math.radians(dy)
        return math.sqrt(lx * lx + ly * ly)

    @staticmethod
    def get_time():
        time = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        return time
