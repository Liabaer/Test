import json

x = json.dumps(
    {'requesterContact': {'phone': u'0106000001', 'name': u'\u5409\u9686\u5761\u8d85\u5e02\u6d4b\u8bd5/kualatest'},
     'serviceType': 'MOTORCYCLE', 'deliveries': [{
        'remarks': 'EASI order id: 26649758\nOrder sn code: X766\nCustomer address remark: \xe5\x90\x89\xe9\x9a\x86\xe5\x9d\xa1\xe6\xb5\x8b\xe8\xaf\x95\nCustomer address house number: S456 Pls contact +60182323299/+60182502559  if cnt contact pick up point and drop off point',
        'toContact': {'phone': u'0106000000', 'name': u'yyy'},
        'toStop': 1}], 'stops': [
        {'location': {'lat': '3.156684', 'lng': '101.67132'}, 'addresses': {'ms_MY': {
            'displayString': u'Jalan Duta, Taman Duta, Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia',
            'country': 'MY_KUL'}}}, {'location': {'lat': '3.134073', 'lng': '101.755073'}, 'addresses': {
            'ms_MY': {'displayString': u'Jalan Pandan Indah, Pandan Indah, Kuala Lumpur, Selangor, Malaysia',
                      'country': 'MY_KUL'}}}]})

print(x)
