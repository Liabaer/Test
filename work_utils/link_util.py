import json
import time
import urllib
import uuid

import requests

header = {'Content-Type': 'application/x-www-form-urlencoded'}
uuid_str = str(uuid.uuid1()).replace('-', '')
vrp_link = ''
data_digest = ''
x = {
    "planRouteParam": {
        "orderParamList": [
            {
                "orderId": "21435897",
                "status": "preparing",
                "deliveryJob": {
                    "latitude": -37.81596,
                    "readyTime": "1617305365",
                    "longitude": 145.121635,
                    "serviceTime": "1M",
                    "dueTime": "1617305725"
                },
                "pickUpJob": {
                    "latitude": -37.816033,
                    "readyTime": "1617305129",
                    "longitude": 145.121612,
                    "serviceTime": "2M",
                    "dueTime": "1617305489"
                }
            },
            {
                "orderId": "21436210",
                "status": "preparing",
                "deliveryJob": {
                    "latitude": -37.857932,
                    "readyTime": "1617304990",
                    "longitude": 145.094842,
                    "serviceTime": 20.0,
                    "dueTime": "1617305170"
                },
                "pickUpJob": {
                    "latitude": -37.857932,
                    "readyTime": "1617305710",
                    "longitude": 145.094842,
                    "serviceTime": 20.0,
                    "dueTime": "1617306070"
                }
            }
        ],
        "easiRider": {
            "latitude": -37.911291,
            "startTime": "1617305365",
            "longitude": 145.122944
        }
    }
}
para = {
    u'logistic_provider_id': u"",
    u'to_code': u"",
    u'msg_type': u"",
    u'msg_id': uuid_str,
    u'data_digest': data_digest,
    u'logistics_interface': json.dumps(x)
}
para = urllib.urlencode(para)
r = requests.post(vrp_link, data=para, headers=header, timeout=10.000)

print(r.json())
