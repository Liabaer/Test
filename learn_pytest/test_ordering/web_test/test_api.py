# -*- coding: utf-8 -*-
import requests

# 顾客
# res = requests.post('http://127.0.0.1:8080/create_customer', headers={'Content-Type': 'application/json'},
#                     json={'amount': 100, 'name': 'tututu', 'password': 'abc123abc123', 'create_time': Job.get_time()})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/customer_login', headers={'Content-Type': 'application/json'},
#                     json={'name': 'tututu', 'password': 'abc123abc123'})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/customer_charge', headers={'Content-Type': 'application/json'},
#                     json={'amount': 11.99, 'type': 1,'token': 'WLI2wOj3A54lAi'})
# print(res.content)


# 商家
# res = requests.post('http://127.0.0.1:8080/create_shop', headers={'Content-Type': 'application/json'},
#                     json={'name': 'shop001', 'password': 'abc123123abc11','status': 0, 'review_score_avg': 0.00,'review_count': 0})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/get_shop_score', headers={'Content-Type': 'application/json'},
#                     json={'shop_id': 1})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/update_business', headers={'Content-Type': 'application/json'},
#                     json={'shop_id': 1,'status': 1})
# print(res.content)

# # 订单
# res = requests.post('http://127.0.0.1:8080/create_order', headers={'Content-Type': 'application/json'},
#                     json={'amount': 11.99, 'shop_id': 1,'token': 'WLI2wOj3A54lAi'})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/completed_order', headers={'Content-Type': 'application/json'},
#                     json={'order_id': 1})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/review_order', headers={'Content-Type': 'application/json'},
#                     json={'order_id': 1,'content':'这里是评论', 'shop_score':65})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/update_order', headers={'Content-Type': 'application/json'},
#                     json={'review_id': 1,'new_content':'这里是新改的评论'})
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/delete_review', headers={'Content-Type': 'application/json'},
#                     json={'review_id': 1})
# print(res.content)

# 0 无权限 2评论审核员 3 admin权限
# res = requests.post('http://127.0.0.1:8080/create_admin', headers={'Content-Type': 'application/json'},
#                     json={'name': 'tututu', 'password': 'abc123abc123','rule':3,'create_time': Job.get_time()})
# print(res.content)

#
# res = requests.post('http://127.0.0.1:8080/agree_audit', headers={'Content-Type': 'application/json'},
#                     json={'admin_id': 1, 'review_id': 1})
# print(res.content)


res = requests.post('http://127.0.0.1:8080/reject_audit', headers={'Content-Type': 'application/json'},
                    json={'reject_reason': '这里是拒绝理由', 'admin_id': 1, 'review_id': 1})
print(res.content)
