import requests
import time
import hmac
import hashlib
import json

key = ''
secret = ''
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
url = ""

headers = {
    'Content-type': 'application/json; charset=utf-8',
    'Authorization': "hmac {key}:{timestamp}:{signature}".format(key=key, timestamp=timestamp, signature=signature),
    'Accept': 'application/json',
    'X-LLM-Market': region
}
r = requests.get(url + path, data=json.dumps(body), headers=headers)

requestTime = (int(round(time.time() * 1000)) - startTime)
print("Total elapsed http request/response time in milliseconds: {}".format(requestTime))
print("Authorization header: hmac {key}:{timestamp}:{signature}".format(
    key=key, timestamp=timestamp, signature=signature))
print("Status Code: {}".format(r.status_code))
print("Returned data: {}".format(r.json()))
