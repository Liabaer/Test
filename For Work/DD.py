import json
import urllib
import uuid

import requests

header = {'Content-Type': 'application/x-www-form-urlencoded'}

uuid_str = str(uuid.uuid1()).replace('-', '')

vrp_link = 'http://link.cainiao.com/gateway/link.do'
data_digest = '23fahiqu3yf=='
x = {
    "planRouteParam":{
        "orderParamList":[
            {
                "orderId":"20973566",
                "status":"wait_pickup",
                "deliveryJob":{
                    "latitude":-37.81596,
                    "readyTime":"2021-03-18T19:41:21",
                    "longitude":145.121635,
                    "serviceTime":10,
                    "dueTime":"2021-03-18T19:47:21"
                },
                "pickUpJob":{
                    "latitude":-37.816033,
                    "readyTime":"2021-03-18T19:29:21",
                    "longitude":145.121612,
                    "serviceTime":15,
                    "dueTime":"2021-03-18T19:32:21"
                }
            },
            {
                "orderId":"20973849",
                "status":"wait_pickup",
                "deliveryJob":{
                    "latitude":-37.857932,
                    "readyTime":"2021-03-18T20:03:54",
                    "longitude":145.094842,
                    "serviceTime":20,
                    "dueTime":"2021-03-18T20:09:54"
                },
                "pickUpJob":{
                    "latitude":-37.857932,
                    "readyTime":"2021-03-18T19:51:54",
                    "longitude":145.094842,
                    "serviceTime":20,
                    "dueTime":"2021-03-18T19:54:54"
                }
            }
        ],
        "easiRiderParam":{
            "latitude":-37.911291,
            "startTime":"2021-03-18T19:54:54",
            "longitude":145.122944
        },
        "taskCode":"11111111111111111"
    }
}
para = {
    u'logistic_provider_id': u"wuLiuYun",
    u'to_code': u"greedSolver",
    u'msg_type': u"RIDER_ROUTE_SERVICE",
    u'msg_id': uuid_str,
    u'data_digest': data_digest,
    u'logistics_interface': json.dumps(x)
}
para = urllib.urlencode(para)
r = requests.post(vrp_link, data=para, headers=header, timeout=10.000)

print json.dumps(r.json())