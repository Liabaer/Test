# -*- coding: utf-8 -*-
import hashlib
import uuid
import requests

# grab日志查询
grab_url = U''
account = U''
secret_easi = U''
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
print(response.content)
