# -*- coding: utf-8 -*-
import datetime

# 设置具体的时间
date = '2019-02-10'
# # 通过split函数把字符串按照-分割成字符串数组
# new_date = date.split('-')
# set_now_start = datetime.datetime.strptime(date, '%Y-%m-%d')
# set_now_end = datetime.datetime.strptime(new_date[0] + '-01-01', '%Y-%m-%d')


# 设置具体的时间
date = '2019-02-10'

set_now_start = datetime.datetime.strptime(date, '%Y-%m-%d')
set_now_end = datetime.datetime.strptime(str(set_now_start.year) + '-01-01', '%Y-%m-%d')
restime = set_now_start - set_now_end
print(restime.days)
