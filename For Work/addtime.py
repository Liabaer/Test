# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime, timedelta

DATE_TIME_FORMAT = '%Y.%m.%d %H:%M:%S'
create_time = '2021.07.30 13:12:58' # 商家接单时间
shop_busy_extras_ready_minutes = 0
preparation_merchant_delay_minutes = 0
shop_special_ready_time_period = '{"special_ready_time_period": [], "ready_minutes": 30}'
shop_ready_time = json.loads(shop_special_ready_time_period)
ready_time = shop_ready_time['ready_minutes'] if 'ready_minutes' in shop_ready_time else 0
base_time = datetime.strptime(
            create_time,
            DATE_TIME_FORMAT
        )
h = str(base_time.hour)
m = str(base_time.minute).zfill(2)
now = h + m

if 'special_ready_time_period' in shop_ready_time:
            for item in shop_ready_time['special_ready_time_period']:
                if int(item['start_time']) <= int(now) < int(item['end_time']):
                    ready_time = item['ready_time']
expect_order_ready_time = base_time + timedelta(minutes=ready_time)

# 预计时间需要加上[忙碌备餐加时]、[商家手动备餐加时]
expect_order_ready_time = expect_order_ready_time + timedelta(
    minutes=shop_busy_extras_ready_minutes
) + timedelta(
    minutes=preparation_merchant_delay_minutes
)
now =datetime.now()

now = now + timedelta(minutes=120)
print (expect_order_ready_time - now).total_seconds() / 60