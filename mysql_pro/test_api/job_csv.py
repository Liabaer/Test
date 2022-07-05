# -*- coding: utf-8 -*-
import csv


class ReadCsv(object):
    @staticmethod
    def read_csv(url):
        f = open(url, 'r')
        # r = csv.reader(f)
        res = []
        for i in f:
            # i是每一列csv的数组
            res.append(i.split(' '))
        f.close()
        # 第一行是标题不要
        return res[1:]