

import requests
import time
import hmac
import hashlib
import json

key = 'pk_test_2847b3958c7b28e39fb49ae4811b2685'  # put your lalamove API key here
secret = 'sk_test_KH+PhVjTbAjMqHGQjD/9EK8rn3SCsMkSJWSYaP0W/xH4hzNEgw/y96J4DEr4l4WQ'  # put your lalamove API secret here

path = '/v2/orders'
region = 'MY_KUL'
method = 'POST'
timestamp = int(round(time.time() * 1000))
body = {
    "serviceType": "CAR",
    "specialRequests": [],
    "requesterContact": {
        "name": "test",
        "phone": "0899183138"
    },
    "stops": [
        {
            "location": {
                "lat": "3.136354",
                "lng": "101.69705"
            },
            "addresses": {
                "ms_MY": {
                    "displayString": "Lorong 23 Geylang, Singapore Badminton Hall, test",
                    "market": region
                }
            }
        },
        {
            "location": {
                "lat": "3.136354",
                "lng": "101.69705"
            },
            "addresses": {
                "ms_MY": {
                    "displayString": "Stamford Road, National Museum of Singapore, test",
                    "market": region
                }
            }
        }
    ],
    "deliveries": [
        {
            "toStop": 1,
            "toContact": {
                "name": "dodo",
                "phone": "+660923447537"
            },
            "remarks": "test"
        }
    ],
    "quotedTotalFee": {
        "amount": "11.80",  # this is value from Quotation response, update it if needed
        "currency": "MYR"
    }
}

rawSignature = "{timestamp}\r\n{method}\r\n{path}\r\n\r\n{body}".format(
    timestamp=timestamp, method=method, path=path, body=json.dumps(body))
signature = hmac.new(secret.encode(), rawSignature.encode(),
                     hashlib.sha256).hexdigest()
startTime = int(round(time.time() * 1000))
url = "https://rest.sandbox.lalamove.com"

headers = {
    'Content-type': 'application/json; charset=utf-8',
    'Authorization': "hmac {key}:{timestamp}:{signature}".format(key=key, timestamp=timestamp, signature=signature),
    'Accept': 'application/json',
    'X-LLM-Market': region
}
r = requests.post(url+path, data=json.dumps(body), headers=headers)

requestTime = (int(round(time.time() * 1000)) - startTime)
print("Total elapsed http request/response time in milliseconds: {}".format(requestTime))
print("Authorization header: hmac {key}:{timestamp}:{signature}".format(
    key=key, timestamp=timestamp, signature=signature))
print("Status Code: {}".format(r.status_code))
print("Returned data: {}".format(r.text))