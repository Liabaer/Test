# -*- coding: utf-8 -*-
import requests

from study_project.test_api.test_public import Job

# res = requests.post('http://127.0.0.1:8080/register_use_new', headers={'Content-Type': 'application/json'},
#                     json={'name': 'yanxu','password': 'abc123', 'type':1})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/register_courier_new', headers={'Content-Type': 'application/json'},
#                     json={'name': 'AAAABBB','password': '123abc'})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/user_login_new', headers={'Content-Type': 'application/json'},
#                     json={'name': 'auynx','password': 'abc123'})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/courier_login_new', headers={'Content-Type': 'application/json'},
#                     json={'name': 'yx-HH','password': '123abc'})
# print(res.content)     0QJlOG6o4SsvT5

#
# res = requests.post('http://127.0.0.1:8080/place_order', headers={'Content-Type': 'application/json'},
#                     json={'user_token': 'Ba1XJK4RF9oLvf'})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/send_order', headers={'Content-Type': 'application/json'},
#                     json={'user_token': 'XSBYa46ymWfm06','courier_id':2,'order_id':1})
# print(res.content)
#
# res = requests.post('http://127.0.0.1:8080/send_order', headers={'Content-Type': 'application/json'},
#                     json={'user_token': 'XSBYa46ymWfm06','courier_id':3,'order_id':1})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/bulk_allocation', headers={'Content-Type': 'application/json'},
#                     json={'user_token': 'XSBYa46ymWfm06','courier_id_list':[3,2,1],'order_id':4})
# print(res.content)


res = requests.post('http://127.0.0.1:8080/accepted_order', headers={'Content-Type': 'application/json'},
                    json={'courier_token': '0QJlOG6o4SsvT5','order_id':4})
print(res.content)

# res = requests.get('http://127.0.0.1:8080/get_courier_bulk_list', headers={'Content-Type': 'application/json'},
#                    params={'courier_token':'0QJlOG6o4SsvT5'})
# print(res.content)

