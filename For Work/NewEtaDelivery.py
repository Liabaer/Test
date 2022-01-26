# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

DATE_TIME_FORMAT = '%Y.%m.%d %H:%M:%S'

from math import radians, sin, cos, asin, sqrt


def distance(lat1, lng1, lat2, lng2):
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = [radians(x) for x in [lng1, lat1, lng2, lat2]]

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6378.137  # 地球平均半径，单位为公里
    return c * r * 1000


shop_lat = -37.813363
shop_lon = 144.973776
courier_lat = -37.808562
courier_lon = 144.963196
dis = distance(shop_lat, shop_lon, courier_lat, courier_lon)

# config
pickupeta = [{"start": 0, "end": 1000, "time": 600}, {"start": 1001, "end": 2000, "time": 780},
             {"start": 2001, "end": 3000, "time": 1200}, {"start": 3001, "end": 4000, "time": 1500},
             {"start": 4001, "end": -1, "time": 1800}]
order_dis = 1369

configs = sorted(pickupeta, key=lambda s: s['start'])
for conf in configs:
    if conf['start'] <= dis <= conf['end']:
        eta_time = conf['time']
        break
    if order_dis >= conf['start'] and conf['end'] == -1:
        eta_time = conf['time']
        break

print 'pickup_eta' + str(eta_time)

deliveryeta = [{"start": 0, "end": 1000, "time": 900}, {"start": 1001, "end": 2000, "time": 1680},
               {"start": 2001, "end": 3000, "time": 1800}, {"start": 3001, "end": 4000, "time": 2040},
               {"start": 4001, "end": 5000, "time": 2280}, {"start": 5001, "end": 8000, "time": 3000},
               {"start": 8001, "end": -1, "time": 3900}]

configs = sorted(deliveryeta, key=lambda s: s['start'])

delivery_time = 300
order_dis = 1400
for conf in configs:
    if conf['start'] <= order_dis <= conf['end']:
        delivery_time = conf['time']
        break
    if order_dis >= conf['start'] and conf['end'] == -1:
        delivery_time = conf['time']
        break
print 'delivery_eta' + str(delivery_time)

order_delivery_eta_modulus = {"modulus": 0.27, "fixed": 6}

delivery_time = (delivery_time * 1.27 + 360 ) /60
print delivery_time + (eta_time/60)

order_pickup_time = '2021.07.30 18:57:20'
now = datetime.now()

now = now + timedelta(minutes=120)
print (datetime.strptime(order_pickup_time, DATE_TIME_FORMAT) + timedelta(minutes=delivery_time) - now).total_seconds() / 60
