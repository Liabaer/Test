

import requests
import time
import hmac
import hashlib
import json

key = 'pk_test_2847b3958c7b28e39fb49ae4811b2685'  # put your lalamove API key here
secret = 'sk_test_KH+PhVjTbAjMqHGQjD/9EK8rn3SCsMkSJWSYaP0W/xH4hzNEgw/y96J4DEr4l4WQ'  # put your lalamove API secret here
order_id = 135660403334
path = '/v2/orders/' + str(order_id)
region = 'MY_KUL'
method = 'GET'
timestamp = int(round(time.time() * 1000))
body = {

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
r = requests.get(url+path, data=json.dumps(body), headers=headers)

requestTime = (int(round(time.time() * 1000)) - startTime)
print("Total elapsed http request/response time in milliseconds: {}".format(requestTime))
print("Authorization header: hmac {key}:{timestamp}:{signature}".format(
    key=key, timestamp=timestamp, signature=signature))
print("Status Code: {}".format(r.status_code))
print("Returned data: {}".format(r.json()))