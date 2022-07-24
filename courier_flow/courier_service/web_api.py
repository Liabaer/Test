# -*- coding: utf-8 -*-
from flask import Flask, request

from courier_flow.courier_model.admin import Admin
from courier_flow.courier_model.audit_record import AuditRecord
from courier_flow.courier_model.courier import Courier
from courier_flow.courier_service.admin_service import AdminService
from courier_flow.courier_service.audit_service import AuditService
from courier_flow.courier_service.courier_service import CourierService

app = Flask(__name__)


@app.route('/register_courier', methods=['POST'])
def register_courier():
    phone_number = request.json.get('phone_number')
    name = request.json.get('name')
    status = request.json.get('status')
    create_time = request.json.get('create_time')
    password = request.json.get('password')
    is_ready = request.json.get('is_ready')
    id_card = request.json.get('id_card')
    courier = Courier(phone_number=phone_number, name=name, status=status, create_time=create_time, password=password,
                      is_ready=is_ready, id_card=id_card)
    CourierService.register_courier(courier)
    return {
        'success': True
    }


@app.route('/courier_login', methods=['POST'])
def courier_login():
    phone_number = request.json.get('phone_number')
    password = request.json.get('password')
    token = CourierService.courier_login(phone_number, password)
    return {
        'token': token
    }


@app.route('/courier_info', methods=['GET'])
def courier_info():
    token = request.args.get('token')
    courier_info_list = CourierService.get_courier(token)
    return {
        'res': courier_info_list
    }


@app.route('/register_admin', methods=['POST'])
def register_admin():
    name = request.json.get('name')
    phone_number = request.json.get('phone_number')
    password = request.json.get('password')
    admin = Admin(name=name, phone_number=phone_number, password=password)
    AdminService.register_admin(admin)
    return {
        'success': True
    }


# 这个不用单独测试
@app.route('/add_audit', methods=['POST'])
def add_audit():
    courier_id = request.json.get('courier_id')
    status = request.json.get('status')
    create_time = request.json.get('create_time')
    audit = AuditRecord(courier_id=courier_id, status=status, create_time=create_time)
    AuditService.add_audit(audit)
    return {
        'success': True
    }


@app.route('/get_audit_list', methods=['GET'])
def get_audit_list():
    audit_list = AuditService.get_audit_list()
    return {
        'res': audit_list
    }


@app.route('/agree_audit', methods=['POST'])
def agree_audit():
    audit_id = request.json.get('audit_id')
    admin_id = request.json.get('admin_id')
    AuditService.agree_audit(audit_id=audit_id, admin_id=admin_id)
    return {
        'res': True
    }


@app.route('/reject_audit', methods=['POST'])
def reject_audit():
    audit_id = request.json.get('audit_id')
    admin_id = request.json.get('admin_id')
    reject_reason = request.json.get('reject_reason')
    AuditService.reject_audit(audit_id=audit_id, admin_id=admin_id, reject_reason=reject_reason)
    return {
        'res': True
    }


app.run(host='127.0.0.1', port=8080, debug=True)
