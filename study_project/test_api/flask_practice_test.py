# -*- coding: utf-8 -*-
import requests

# response = requests.post('http://127.0.0.1:8080/user/register', headers={'Content-Type': 'application/json'},
#                          json={"name":"tututu","password":"abc123123","email":"123123123@qq.com","phone_number":"135811111"})
# print(response.content)


# response = requests.post('http://127.0.0.1:8080/user/login', headers={'Content-Type': 'application/json'},
#                          json={"name":"tututu","password":"abc123123"})
# print(response.content)

res = requests.post("http://127.0.0.1:8080/user/update-password",headers={'Content-Type': 'application/json','token':'l5w2p3i9l3i8w0z7'},
                    json={"pwd":"abc123123",'new_pwd':"112233aabbcc"})

print(res.content)