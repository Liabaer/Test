# -*- coding: utf-8 -*-
import datetime

# 获取当前时间 年月日格式
today = datetime.date.today()
print(today)
# 获取时间对象的年月日
print(today.year)
print(today.month)
print(today.day)
# 获取当前日期是礼拜几
print(today.isoweekday())

# 设置日期
set_date = datetime.date(2022, 2, 1)
print(set_date)

diff_time = today - set_date
# total_seconds 计算2个时间相差了多少秒
# days 相差了多少天
print('相差了多少天 这里用total_seconds除以了秒数', diff_time.total_seconds() / (60 * 60 * 24))
print('相差了多少天', diff_time.days)

# 获取当前时间 精确到秒
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 设置具体的时间
set_now = datetime.datetime.strptime("2022.02.01 00:00:00", '%Y.%m.%d %H:%M:%S')
print(set_now)

