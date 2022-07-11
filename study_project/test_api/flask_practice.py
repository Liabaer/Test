# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from mysql_pro.test_api.user_service import UserService
from mysql_pro.test_api.user import User

# 初始化
app = Flask(__name__)


@app.route('/user/register', methods=['POST'])
def test_user_register():
    """
    用户注册
    :return:
    """
    name = request.json.get("name")
    password = request.json.get("password")
    email = request.json.get("email")
    phone_number = request.json.get("phone_number")
    user = User(name=name, email=email, phone_number=phone_number, password=password)
    UserService.register_user(user)
    return {
        "data": {
            "success": True
        },
        "errorMessage": ""
    }


@app.route('/user/login', methods=['POST'])
def test_user_login():
    """
    用户登录
    :return:
    """
    name = request.json.get("name")
    password = request.json.get("password")
    token = UserService.user_login(user_name=name, pwd=password)
    return {
        "data": {
            "token": token
        }
    }


@app.route('/user/update-password', methods=['POST'])
def test_user_update_pwd():
    """
    用户修改密码
    :return:
    """
    pwd = request.json.get("password")
    new_pwd = request.json.get("new_pwd")
    UserService.update_pwd(token=request.headers.get('token'), pwd=pwd, new_pwd=new_pwd)
    return {
        "data": {
            "token": True
        }
    }


# 运行后端服务，后端服务有以上接口，端口是8080，host是127.0.0.1,debug开启
app.run(host="127.0.0.1", port=8080, debug=True)
