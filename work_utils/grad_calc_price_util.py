# -*- coding: utf-8 -*-
import hashlib
import uuid

import requests

# grab计价工具类

grab_url = U''
account = U''
secret_easi = U''
uuid_str = str(uuid.uuid1()).replace('-', '')
print(uuid_str)
# 加密
fp_token = hashlib.sha1(account + uuid_str + secret_easi).hexdigest()
print(fp_token)

headers = {
    'fp-account': account,
    'fp-uid': uuid_str,
    'fp-token': fp_token,
    'Content-Type': 'application/json'
}
# 计价接口
data = {"merchantOrderID": "11025133", "origin": {"coordinates": {"latitude": 3.133892, "longitude": 101.7516751},
                                                  "address": "Persiaran Saujana Putra, Kampung Lombong, Shah Alam, Selangor, Malaysia"},
        "serviceType": "INSTANT", "packages": [{"price": 0,
                                                "description": "EASI order id: 11025133\nOrder sn code: K106\nCustomer address remark: \u8fd9\u91cc\u662f\u5730\u5740\u5907\u6ce8\u5594\uff01grab\u80fd\u4e0d\u80fd\u6536\u5230\uff0c\u6211\u4e5f\u4e0d\u77e5\u9053\u5594\nCustomer address house number: j88\u5566\u5566\nCustomer remark: ",
                                                "dimensions": {"width": 0, "depth": 0, "weight": 0, "height": 0},
                                                "name": "easi", "quantity": 0}],
        "sender": {"smsEnabled": True, "phone": "", "email": "ssbur@gmail.com", "firstName": "test pho",
                   "companyName": "test pho"}, "paymentMethod": "CASHLESS",
        "destination": {"coordinates": {"latitude": 2.9516899, "longitude": 101.577759},
                        "address": "Pandan Indah, Kuala Lumpur, Selangor, Malaysia"},
        "recipient": {"smsEnabled": True, "lastName": "Tan", "email": "jo@gmail.com", "firstName": "John",
                      "phone": "0100000001"}}

quote_url = grab_url + u'/api/logistics/grab/delivery'
response = requests.post(quote_url, headers=headers, json=data, timeout=10.0)
print(response.content)
