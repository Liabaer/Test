# -*- coding: utf-8 -*-
# 网络请求第三方库 requests 知识

# http请求方法常见有GET、POST、PUT、DELETE等（后面三种方式大同小易）

# GET 请求

import requests

# response = requests.get("https://www.baidu.com/")
# # response是返回的一个类对象
# # 调用content对象返回接口的详情，我们这里访问的是百度，所以返回的肯定是一个百度的网页
# print(response.content)
# # 返回请求的状态200是成功，403是没权限、400是参数错误，500是服务错误（常见http状态码）
# print(response.status_code)
#
# # 上面的写法没有传入参数，如果我们需要对get请求传入参数
# response = requests.get("https://www.baidu.com/", params={'username': 'liabaer', 'password': 'yanxu'})
# # 打印我们的实际请求路径，get的请求的参数是放在url上面的
# print(response.url)
#
# # 传入header
# response = requests.get("https://www.baidu.com/", headers={'User-Agent': 'Mozilla'})
#
# # post请求和上面一样，区别在于传入参数的方式不同,这里我们调用百度的登录接口
# r = requests.post('https://passport.baidu.com/v2/api/?login',
#                   headers={"Content-Type": "application/x-www-form-urlencoded"},
#                   data={'username': '234234234234', 'password': '123456'})
# print(r.content)
# print(r.status_code)
# 200表示请求成功获取返回的数据，接口返回数据内容放在json()中，是一个字典
# if r.status_code == 200:
#     print(r.status_code)
#     print(r.json())
# else:
#     print("接口报错")
#     print(r.status_code)



# 域名
# http://183.71.250.130:10001
# 测试账号
# 邮箱RenaTuT0401@gmail.com
# 密码34dfsdAf324sf2@s
#
# 第一步
hd = {'language': 'cn','device':'tt-test','Content-Type':'application/json'}
pwd = {'email':'RenaTuT0401@gmail.com','password':'34dfsdAf324sf2@s'}
url = 'http://183.71.250.130:10001'

res = requests.post(url+'/api/user/pre-login',
                    headers=hd,
                    json=pwd)
print(res.json())
# print(res.content)

# 预登录接口 /api/user/pre-login POST
# 请求参数字段email password
# header  language: cn device: tt-test Content-Type: application/json
#
# 第二步
# 获取上面接口的返回值 authId字段
auth = res.json().get('data').get('authId')
# print(auth)
# 第三步
# 发送邮箱验证码接口 /api/user/auth-email POST
# 请求参数字段 authId  emailType(等于login_auth)
# header  language: cn device: tt-test Content-Type: application/json
eml = requests.post(url + '/api/user/auth-email',
                    headers=hd,
                    json={'authId':auth,'emailType':'login_auth'})
print(eml)
email_code = input()
#
# 根据邮箱中的验证码进行第四步
#
# 第四步
# 调用实际的登录接口 /api/user/auth
# 请求入参字段authId  authType(等于email_auth)  authText(等于邮箱中的验证码) operator(等于login)
# header  language: cn device: tt-test Content-Type: application/json
lgn = requests.post(url+'/api/user/auth',
                      headers=hd,
                      json={'authId':auth,'authType':'email_auth','authText':email_code,'operator':'login'})
print(lgn.json())
# 获取返回值中的token字段 ，则表示登录成功，上述流程通过一个python文件执行完流程。