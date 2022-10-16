# -*- coding: utf-8 -*-
import json

date = {'id': 8242, 'uncompleted_order_id_list': [], 'last_complete_time': '2021.08.10 18:31:23', 'driving_type': 1,
        'tag': '8,12,52,92', 'language': 'cn', 'display_name': 'TEST-Jason', 'score': -25, 'basic_unit': 115,
        'location': ['-37.808566', '144.963196'], 'has_profile_image': True, 'delivery_type': 0,
        'delivery_fee_today': '0', 'communication_language': 'cn,en,ja,ms'}
print(json.dumps(date))
