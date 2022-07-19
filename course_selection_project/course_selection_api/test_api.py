# -*- coding: utf-8 -*-
import requests

# res = requests.post('http://127.0.0.1:8080/create_book',headers={'Content-Type': 'application/json'},
#                     json={'name':'python','book_category':1,'count':10})
# print(res.content)
#
# res = requests.post('http://127.0.0.1:8080/create_book_cate',headers={'Content-Type': 'application/json'},
#                     json={'name':'python','book_category':1,'count':10})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/create_card', headers={'Content-Type': 'application/json'},
#                     json={'name':'tututu', 'amount':100})
# print(res.content)
#
# res = requests.post('http://127.0.0.1:8080/use_card', headers={'Content-Type': 'application/json'},
#                     json={'type': 1, 'amount': 10, 'card_id': 2})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/borrow', headers={'Content-Type': 'application/json'},
#                     json={'book_id': 1, 'card_id': 2})
# print(res.content)


res = requests.post('http://127.0.0.1:8080/get_audit', headers={'Content-Type': 'application/json'},
                    json={'book_id': 1, 'card_id': 2})
print(res.content)