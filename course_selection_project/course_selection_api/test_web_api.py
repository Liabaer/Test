# -*- coding: utf-8 -*-
import requests

# res = requests.post('http://127.0.0.1:8080/school_user/login', headers={'Content-Type': 'application/json'},
#                     json={'id': 2, 'name': 'yanxu', 'password': 'abc123abc123'})
#
# print(res.content)
#
res = requests.post('http://127.0.0.1:8080/school_user/choose_cls', headers={'Content-Type': 'application/json'},
                    json={'token': 'MkZM6vWdi7LCFN', 'class_id': 1})

print(res.content)

# res = requests.post('http://127.0.0.1:8080/school_user/register', headers={'Content-Type': 'application/json'},
#                     json={'url':'user_register.csv'})
#
# print(res.content)

# res = requests.get('http://127.0.0.1:8080/school_user/get_cls', headers={'Content-Type': 'application/json'})
#
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/school_user/create_cls', headers={'Content-Type': 'application/json'},
#                     json={'token':'Ih19dYvtLv5_9s', 'name': 'python', 'teach_id': 2, 'count': 10, 'start_time': '2022.07.20 00:00:00',
#                           'end_time': '2022.08.30 00:00:00'})
#
# print(res.content)
