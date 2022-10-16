# -*- coding: utf-8 -*-
import requests

# res = requests.post('http://127.0.0.1:8080/register_user', headers={'Content-Type': 'application/json'},
#                     json={'name': 'tututu', 'amount': 100.00, 'password': 'aabbcc123', 'create_time': Job.get_time()})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/user_login', headers={'Content-Type': 'application/json'},
#                     json={'name': 'tututu', 'password': 'aabbcc123'})
# print(res.content)      7gNB2qp GAMxLC


# res = requests.post('http://127.0.0.1:8080/register_courier', headers={'Content-Type': 'application/json'},
#                     json={'name': 'liabear', 'amount': 1.00, 'password': 'aabbcc123', 'create_time': Job.get_time()})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/courier_login', headers={'Content-Type': 'application/json'},
#                     json={'name': 'liabear', 'password': 'aabbcc123'})
# print(res.content)     sicweN2ZpjRvYk


# res = requests.post('http://127.0.0.1:8080/user_charge', headers={'Content-Type': 'application/json'},
#                     json={'token': '7gNB2qp GAMxLC', 'amount': 1.00})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/place_order', headers={'Content-Type': 'application/json'},
#                     json={'user_token': '7gNB2qp GAMxLC', 'amount': 1.99})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/accepted_order', headers={'Content-Type': 'application/json'},
#                     json={'courier_token': 'sicweN2ZpjRvYk', 'order_id': 5})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/completed_order', headers={'Content-Type': 'application/json'},
#                     json={'courier_token': 'sicweN2ZpjRvYk', 'order_id': 5})
# print(res.content)


res = requests.get('http://127.0.0.1:8080/get_settle', headers={'Content-Type': 'application/json'})
print(res.content)
