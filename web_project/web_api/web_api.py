# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

from web_project.web_api.user import User
from web_project.web_api.user_service import UserService

app = Flask(__name__)

@app.route('/user/register-new',methods=['POST'])
def test_user_register():
    phone_number = request.json.get('phone_number')
    password = request.json.get('password')
    user = User(phone_number=phone_number,password=password)
    UserService.user_register(user)
    return {
        'res':True
    }

@app.route('/user/login-new',methods=['POST'])
def test_user_login():
    phone_number = request.json.get('phone_number')
    password = request.json.get('password')
    user = User(phone_number=phone_number,password=password)
    token = UserService.user_login(user)
    return {
        'token':token
    }


# 运行
app.run(host="127.0.0.1", port=8080, debug=True)