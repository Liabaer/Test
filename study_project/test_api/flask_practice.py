# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

# 初始化
app = Flask(__name__)


@app.route('/user/register', method=['GET'])
def test_user_register():
    """
    用户注册
    :return:
    """
    return {
        "data": {
            "name": request.args.get("name"),
            "password": request.args.get("password"),
            "email": request.args.get("email"),
            "phone_number": request.args.get("phone_number")
        },
        "errorMessage": ""
    }


@app.route('/user/login', method=['POST'])
def test_user_login():
    """
    用户登录
    :return:
    """
    return {
        "data": {
            "name": request.json.get("name"),
            "password": request.json.get("password")
        }
    }

@app.route('/user/update-password', method=['POST'])
def test_user_update_pwd():
    """
    用户修改密码
    :return:
    """
    return {
        "data": {

        }
    }

