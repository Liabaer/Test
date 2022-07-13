# -*- coding: utf-8 -*-
import requests

res = requests.post('http://127.0.0.1/school_user/login', headers={'Content-Type': 'application/json'},
                    json={'name': 'tutut', 'password': '123abc123abc'})

print(res.content)

res = requests.post('http://127.0.0.1/school_user/choose_cls', headers={'Content-Type': 'application/json'},
                    json={'token': '', 'class_id': 1})

print(res.content)

res = requests.post('http://127.0.0.1/user_register', headers={'Content-Type': 'application/json'},
                    json={'url':'user_register.csv'})

print(res.content)

res = requests.post('http://127.0.0.1/sget_cls', headers={'Content-Type': 'application/json'})

print(res.content)

res = requests.post('http://127.0.0.1/create_cls', headers={'Content-Type': 'application/json'},
                    json={'name': 'python', 'teach_id': 1, 'count': 10, 'start_time': '2022-07-10',
                          'end_time': '2022-07-30'})

print(res.content)
