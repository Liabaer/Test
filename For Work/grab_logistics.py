# -*- coding: utf-8 -*-
import hashlib
import uuid
import requests

grab_url = U'https://api.presto.express'
account = U'pe-easi-prod'
secret_easi = U'2bZtTk5qlkDAsrX6'
uuid_str = str(uuid.uuid1()).replace('-', '')
# 加密
fp_token = hashlib.sha1(account + uuid_str + secret_easi).hexdigest()
deliveryid = 'IN-2-0E5FE1FACRYUE5IC4136'

headers = {
    'fp-account': account,
    'fp-uid': uuid_str,
    'fp-token': fp_token,
    'Content-Type': 'application/json'
}

quote_url = grab_url + u'/api/logistics/grab/delivery/' + deliveryid
response = requests.get(quote_url, headers=headers, timeout=10.0)
print response.content