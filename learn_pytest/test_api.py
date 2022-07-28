# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pytest
import requests


@pytest.fixture
def first_entry():
    return "a"


class TestApiClass(object):

    # 使用pytest定义一个全局到处都可以使用的函数，在test_user_register中直接传入get_api,这个直接可以获取到这个函数的返回值，这是一个用法，可以记住
    @pytest.fixture
    def get_api(self):
        return 'http://127.0.0.1:8080'

    # 这个函数将会运行三次,前面第一个参数定义了2个参数名，后面第一个参数定义了一个数组，数组里面的是每个元祖，正好是一组前面的参数
    @pytest.mark.parametrize("test_input,out_put", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    @pytest.mark.run(order=3)
    def test_eval(self, test_input, out_put):
        assert eval(test_input) == out_put

    @staticmethod
    @pytest.mark.run(order=2)
    def test_user_register(get_api):
        res = requests.post(get_api + '/register_use_new', headers={'Content-Type': 'application/json'},
                            json={'name': 'yanxu', 'password': 'abc123', 'type': 1})
        # 使用断言判断接口是否响应成功
        assert get_api == 'http://127.0.0.1:8080'
        assert res.status_code == 200

    @staticmethod
    @pytest.mark.run(order=1)
    def test_courier_register():
        res = requests.post('http://127.0.0.1:8080/register_courier_new', headers={'Content-Type': 'application/json'},
                            json={'name': 'AAAABBB', 'password': '123abc'})
        assert res.status_code == 200

    @staticmethod
    def test_user_login():
        res = requests.post('http://127.0.0.1:8080/user_login_new', headers={'Content-Type': 'application/json'},
                            json={'name': 'auynx', 'password': 'abc123'})
        assert res.status_code == 200

    @staticmethod
    def test_courier_login():
        res = requests.post('http://127.0.0.1:8080/courier_login_new', headers={'Content-Type': 'application/json'},
                            json={'name': 'yx-HH', 'password': '123abc'})
        assert res.status_code == 200

    @pytest.mark.slow
    def test_place_order(self):
        res = requests.post('http://127.0.0.1:8080/place_order', headers={'Content-Type': 'application/json'},
                            json={'user_token': 'Ba1XJK4RF9oLvf'})
        assert res.status_code == 200

    @pytest.mark.slow
    def test_send_order(self):
        res = requests.post('http://127.0.0.1:8080/send_order', headers={'Content-Type': 'application/json'},
                            json={'user_token': 'XSBYa46ymWfm06', 'courier_id': 2, 'order_id': 1})
        assert res.status_code == 200

    @staticmethod
    def test_bulk_allocation():
        res = requests.post('http://127.0.0.1:8080/bulk_allocation', headers={'Content-Type': 'application/json'},
                            json={'user_token': 'XSBYa46ymWfm06', 'courier_id_list': [3, 2, 1], 'order_id': 4})
        assert res.status_code == 200

    @staticmethod
    def test_accepted_order():
        res = requests.post('http://127.0.0.1:8080/accepted_order', headers={'Content-Type': 'application/json'},
                            json={'courier_token': '0QJlOG6o4SsvT5', 'order_id': 4})
        assert res.status_code == 200

    @staticmethod
    def test_get_courier_bulk_list():
        res = requests.get('http://127.0.0.1:8080/get_courier_bulk_list', headers={'Content-Type': 'application/json'},
                           params={'courier_token': '0QJlOG6o4SsvT5'})
        assert res.status_code == 200