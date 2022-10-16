# -*- coding: utf-8 -*-
from flask import Flask, request

from learn_flask.finance.order_finance.finance_model.courier_finance import CourierFinance
from learn_flask.finance.order_finance.finance_model.user_finance import UserFinance
from learn_flask.finance.order_finance.finance_serivce.courier_service import CourierService
from learn_flask.finance.order_finance.finance_serivce.order_finance import OrderFinanceService
from learn_flask.finance.order_finance.finance_serivce.settle_account_service import SettleAccountService
from learn_flask.finance.order_finance.finance_serivce.user_service import UserService

app = Flask(__name__)


# 1. 用户注册

@app.route('/register_user', methods=['POST'])
def register_user():
    amount = request.json.get('amount')
    name = request.json.get('name')
    create_time = request.json.get('create_time')
    password = request.json.get('password')
    user = UserFinance(name=name, password=password, amount=amount, create_time=create_time)
    UserService.register_user(user)
    return {
        'success': True
    }


# 2. 用户登录

@app.route('/user_login', methods=['POST'])
def user_login():
    name = request.json.get('name')
    password = request.json.get('password')
    user = UserFinance(name=name, password=password)
    token = UserService.user_login(user)
    return {
        'token': token
    }


# 3. 用户充值

@app.route('/user_charge', methods=['POST'])
def user_charge():
    amount = request.json.get('amount')
    token = request.json.get('token')
    UserService.user_charge(token, amount)
    return {
        'success': True
    }


# 4. 下单
@app.route('/place_order', methods=['POST'])
def place_order():
    amount = request.json.get('amount')
    user_token = request.json.get('user_token')
    OrderFinanceService.place_order(amount, user_token)
    return {
        'success': True
    }


# 5. 接单
@app.route('/accepted_order', methods=['POST'])
def accepted_order():
    order_id = request.json.get('order_id')
    courier_token = request.json.get('courier_token')
    OrderFinanceService.accepted_order(order_id, courier_token)
    return {
        'success': True
    }


# 6. 完成
@app.route('/completed_order', methods=['POST'])
def completed_order():
    order_id = request.json.get('order_id')
    courier_token = request.json.get('courier_token')
    OrderFinanceService.completed_order(order_id, courier_token)
    return {
        'success': True
    }


# 7. 查询未结算订单列表
@app.route('/get_settle', methods=['GET'])
def get_settle():
    order_list = SettleAccountService.get_unsettle()
    return {
        'data': order_list
    }


# 1. 骑手注册

@app.route('/register_courier', methods=['POST'])
def register_courier():
    amount = request.json.get('amount')
    name = request.json.get('name')
    create_time = request.json.get('create_time')
    password = request.json.get('password')
    courier = CourierFinance(name=name, password=password, amount=amount, create_time=create_time)
    CourierService.register_courier(courier)
    return {
        'success': True
    }


# 2. 骑手登录

@app.route('/courier_login', methods=['POST'])
def courier_login():
    name = request.json.get('name')
    password = request.json.get('password')
    courier = CourierFinance(name=name, password=password)
    token = CourierService.courier_login(courier)
    return {
        'token': token
    }


app.run(host='127.0.0.1', port=8080, debug=True)
