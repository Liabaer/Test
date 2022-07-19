# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

from test_ordering.ordering_model.admin import Admin
from test_ordering.ordering_model.customer import Customer
from test_ordering.ordering_service.admin_service import AdminService
from test_ordering.ordering_service.audit_service import AuditService
from test_ordering.ordering_service.customer_service import CustomerService
from test_ordering.ordering_model.shop import Shop
from test_ordering.ordering_service.order_service import OrderService
from test_ordering.ordering_service.shop_service import ShopService

app = Flask(__name__)


# 顾客
@app.route('/create_customer', methods=['POST'])
def create_customer():
    amount = request.json.get('amount')
    name = request.json.get('name')
    password = request.json.get('password')
    create_time = request.json.get('create_time')
    customer = Customer(amount=amount, name=name, password=password, create_time=create_time)
    res = CustomerService.create_customer(customer)
    return {
        'success': res
    }


@app.route('/customer_login', methods=['POST'])
def customer_login():
    name = request.json.get('name')
    password = request.json.get('password')
    res = CustomerService.customer_login(name=name, password=password)
    return {
        'success': res
    }


@app.route('/customer_charge', methods=['POST'])
def customer_charge():
    amount = request.json.get('amount')
    type = request.json.get('type')
    token = request.json.get('token')
    CustomerService.charge(amount=amount, token=token, type=type)
    return {
        'success': True
    }


# 商家
@app.route('/create_shop', methods=['POST'])
def create_shop():
    review_score_avg = request.json.get('review_score_avg')
    review_count = request.json.get('review_count')
    name = request.json.get('name')
    password = request.json.get('password')
    status = request.json.get('status')
    shop = Shop(name=name, password=password, status=status, review_score_avg=review_score_avg, review_count=review_count)
    res = ShopService.create_shop(shop)
    return {
        'success': res
    }


@app.route('/get_shop_score', methods=['POST'])
def get_shop_score():
    shop_id = request.json.get('shop_id')
    res = ShopService.get_score(shop_id=shop_id)
    return {
        'success': res
    }


@app.route('/update_business', methods=['POST'])
def update_business():
    shop_id = request.json.get('shop_id')
    status = request.json.get('status')
    ShopService.update_business(shop_id=shop_id, status=status)
    return {
        'success': True
    }


# 订单
@app.route('/create_order', methods=['POST'])
def create_order():
    amount = request.json.get('amount')
    shop_id = request.json.get('shop_id')
    token = request.json.get('token')
    OrderService.create_order(token=token, shop_id=shop_id, amount=amount)
    return {
        'success': True
    }


@app.route('/completed_order', methods=['POST'])
def completed_order():
    order_id = request.json.get('order_id')
    OrderService.completed_order(order_id=order_id)
    return {
        'success': True
    }


@app.route('/review_order', methods=['POST'])
def review_order():
    order_id = request.json.get('order_id')
    content = request.json.get('content')
    shop_score = request.json.get('shop_score')
    OrderService.review_order(order_id=order_id, content=content, shop_score=shop_score)
    return {
        'success': True
    }


@app.route('/update_order', methods=['POST'])
def update_order():
    review_id = request.json.get('review_id')
    new_content = request.json.get('new_content')
    OrderService.update_review(review_id=review_id, new_content=new_content)
    return {
        'success': True
    }


@app.route('/delete_review', methods=['POST'])
def delete_review():
    review_id = request.json.get('review_id')
    OrderService.delete_review(review_id=review_id)
    return {
        'success': True
    }


# 管理员
@app.route('/create_admin', methods=['POST'])
def create_admin():
    name = request.json.get('name')
    password = request.json.get('password')
    create_time = request.json.get('create_time')
    rule = request.json.get('rule')
    admin = Admin(name=name, password=password, rule=rule, create_time=create_time)
    AdminService.create_admin(admin)
    return {
        'success': True
    }


# 审核
@app.route('/get_audit', methods=['GET'])
def get_audit():
    type = request.args.get('type')
    res = AuditService.get_audit_list(type)
    return {
        'success': res
    }


@app.route('/agree_audit', methods=['POST'])
def agree_audit():
    admin_id = request.json.get('admin_id')
    review_id = request.json.get('review_id')
    AuditService.agree_audit(admin_id, review_id)
    return {
        'success': True
    }

@app.route('/reject_audit', methods=['POST'])
def reject_audit():
    admin_id = request.json.get('admin_id')
    review_id = request.json.get('review_id')
    reject_reason = request.json.get('reject_reason')
    AuditService.reject_audit(reject_reason, admin_id, review_id)
    return {
        'success': True
    }


app.run(host='127.0.0.1', port=8080, debug=True)
