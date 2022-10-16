# -*- coding: utf-8 -*-

# res = requests.post('http://127.0.0.1:8080/register_courier',headers={'Content-Type': 'application/json'},
#                     json={'name':'tututu222', 'status':0,'create_time':Job.get_time(),
#                           'phone_number':'01234567','password':'aabbcc123', 'is_ready':0,'id_card':'12345678901234567890abcdefgd'})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/courier_login',headers={'Content-Type': 'application/json'},
#                     json={'phone_number':'01234567','password':'aabbcc123'})
# print(res.content)    oKiKRlqNcBmRWt


# res = requests.get('http://127.0.0.1:8080/courier_info',headers={'Content-Type': 'application/json'},
#                     params={'token':'oKiKRlqNcBmRWt'})
# print(res.content)

# res = requests.post('http://127.0.0.1:8080/register_admin',headers={'Content-Type': 'application/json'},
#                     json={'name':'yanxu', 'phone_number':'01234567','password':'aabbcc123'})
# print(res.content)

#
# res = requests.get('http://127.0.0.1:8080/get_audit_list',headers={'Content-Type': 'application/json'},)
# print(res.content)


# res = requests.post('http://127.0.0.1:8080/agree_audit',headers={'Content-Type': 'application/json'},
#                     json={'audit_id':1, 'admin_id':1})
# print(res.content)
#
# res = requests.post('http://127.0.0.1:8080/reject_audit',headers={'Content-Type': 'application/json'},
#                     json={'audit_id':2, 'admin_id':1,'reject_reason': "就是要拒绝你！"})
# print(res.content)
