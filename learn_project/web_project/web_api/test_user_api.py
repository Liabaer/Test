# -*- coding: utf-8 -*-
import requests

res = requests.post('http://127.0.0.1:8080/user/register-new', headers={'Content-Type': 'application/json'},
                    json={'phone_number': 13459999111, 'password': '12b45312bb'})
print(res.content)

response = requests.post('http://127.0.0.1:8080/user/login-new', headers={'Content-Type': 'application/json'},
                         json={'phone_number': 13459999111, 'password': '12b45312bb'})
print(response.content)
