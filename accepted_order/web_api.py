# -*- coding: utf-8 -*-
from flask import Flask, request

from accepted_order.model.user_new import UserNew
from accepted_order.service.courier_service import CourierService
from accepted_order.service.order_service import OrderService
from accepted_order.service.user_service import UserService

app = Flask(__name__)

# 1. 用户注册

@app.route('/register_use_new', methods=['POST'])
def register_user():
    name = request.json.get('name')
    password = request.json.get('password')
    type = request.json.get('type')
    UserService.register_user(name=name,password=password,type=type)
    return {
        'success': True
    }


@app.route('/user_login_new', methods=['POST'])
def user_login():
    name = request.json.get('name')
    password = request.json.get('password')
    token = UserService.user_login(name=name,password=password)
    return {
        'data': token
    }


# 骑手注册
@app.route('/register_courier_new', methods=['POST'])
def register_courier_new():
    name = request.json.get('name')
    password = request.json.get('password')
    CourierService.register_courier(name=name, password=password)
    return {
        'success': True
    }


@app.route('/courier_login_new', methods=['POST'])
def courier_login():
    name = request.json.get('name')
    password = request.json.get('password')
    token = CourierService.courier_login(name=name, password=password)
    return {
        'data': token
    }



# 订单
@app.route('/place_order', methods=['POST'])
def place_order():
    user_token = request.json.get('user_token')
    OrderService.place_order(user_token)
    return {
        'success': True
    }



@app.route('/send_order', methods=['POST'])
def send_order():
    user_token = request.json.get('user_token')
    courier_id = request.json.get('courier_id')
    order_id = request.json.get('order_id')
    OrderService.send_order(user_token, courier_id, order_id)
    return {
        'success': True
    }



@app.route('/bulk_allocation', methods=['POST'])
def bulk_allocation():
    user_token = request.json.get('user_token')
    courier_id_list = request.json.get('courier_id_list')
    order_id = request.json.get('order_id')
    OrderService.bulk_allocation(user_token, courier_id_list, order_id)
    return {
        'success': True
    }




@app.route('/get_courier_bulk_list', methods=['GET'])
def get_courier_bulk_list():
    courier_token = request.args.get('courier_token')
    res_list = OrderService.get_courier_bulk_list(courier_token)
    return {
        'data': res_list
    }



@app.route('/accepted_order', methods=['POST'])
def accepted_order():
    courier_token = request.json.get('courier_token')
    order_id = request.json.get('order_id')
    OrderService.accepted_order(courier_token, order_id)
    return {
        'success': True
    }



app.run(host='127.0.0.1', port=8080, debug=True)