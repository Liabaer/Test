# -*- coding: utf-8 -*-
import requests


res = requests.post('ttp://127.0.0.1:8080/user/register',headers={'Content-Type': 'application/json'},
                    json={'phon_number':1345999911,'password':'12b45312'})
print(res)


response = requests.post('ttp://127.0.0.1:8080/user/login',headers={'Content-Type': 'application/json'},
                    json={'phon_number':1345999911,'password':'12b45312'})
print(response)