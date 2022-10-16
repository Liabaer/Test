# -*- coding: utf-8 -*-
from datetime import timedelta
from datetime import datetime, timedelta

# 取货eta计算

DATE_TIME_FORMAT = '%Y.%m.%d %H:%M:%S'

from math import radians, sin, cos, asin, sqrt

# def distance(lat1, lng1, lat2, lng2):
#     # 将十进制度数转化为弧度
#     lon1, lat1, lon2, lat2 = [radians(x) for x in [lng1, lat1, lng2, lat2]]
#
#     # haversine公式
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#     c = 2 * asin(sqrt(a))
#     r = 6378.137  # 地球平均半径，单位为公里
#     return c * r * 1000
# shop_lat = -42.8763767
# shop_lon = 147.32045730000004
# courier_lat = -42.880224
# courier_lon = 147.331498
#

# dis = distance(shop_lat, shop_lon, courier_lat, courier_lon)

# print(dis)

order_pickup_time = '2021.07.02 17:58:55'

pickupeta = [{"start": 0, "end": 3000, "time": 900}, {"start": 3001, "end": 5000, "time": 1200},
             {"start": 5001, "end": -1, "time": 1800}]
order_dis = 1369

configs = sorted(pickupeta, key=lambda s: s['start'])
print(configs)

eta_time = 300
for conf in configs:
    if conf['start'] <= order_dis <= conf['end']:
        eta_time = conf['time']
        break
    if order_dis >= conf['start'] and conf['end'] == -1:
        eta_time = conf['time']
        break
print(eta_time)

deliveryeta = [{"start": 0, "end": 500, "time": 1200}, {"start": 501, "end": 5000, "time": 1800},
               {"start": 5001, "end": 10000, "time": 2400}, {"start": 10001, "end": 15000, "time": 3000},
               {"start": 15001, "end": -1, "time": 3600}]
order_dis = 1369

configs = sorted(deliveryeta, key=lambda s: s['start'])
print(configs)

delivery_time = 300
for conf in configs:
    if conf['start'] <= order_dis <= conf['end']:
        delivery_time = conf['time']
        break
    if order_dis >= conf['start'] and conf['end'] == -1:
        delivery_time = conf['time']
        break
print(delivery_time)

print((eta_time + delivery_time) / 60)

courier_complete_order_estimated_datetime = datetime.strptime(order_pickup_time, DATE_TIME_FORMAT) + timedelta(
    minutes=int(delivery_time) / 60)
print((courier_complete_order_estimated_datetime - (datetime.now() + timedelta(minutes=120))).total_seconds() / 60)
