# -*- coding: utf-8 -*-
import requests

header = {'Content-Type': 'application/x-www-form-urlencoded'}
para = 'msg_type=CNALGO_GREEDSOLVER_CREATE_TASK&logistics_interface=%7B%22inputParam%22%3A+%7B%22appKey%22%3A+%221F43C0DDC4181A28D914BD57B6F01C7AE2AD9707%22%2C+%22input%22%3A+%22%7B%5C%22problem%5C%22%3A+%7B%5C%22vehicles%5C%22%3A+%5B%7B%5C%22plate%5C%22%3A+%5C%228242%5C%22%2C+%5C%22score%5C%22%3A+100%2C+%5C%22current_location%5C%22%3A+%5C%22144.963196%2C-37.808562%5C%22%2C+%5C%22fixed_cost%5C%22%3A+%5C%22%5C%5Cuffe53%5C%22%2C+%5C%22idle_price%5C%22%3A+%5C%22%5C%5Cuffe50%5C%22%2C+%5C%22valid_radius%5C%22%3A+%5C%221800M%5C%22%2C+%5C%22distance_price%5C%22%3A+%5C%22%5C%5Cuffe52.8%2FKM%5C%22%2C+%5C%22order_capacity%5C%22%3A+5%7D%5D%2C+%5C%22objective.min_labor_fluctuation%5C%22%3A+%7B%5C%22max_overlap%5C%22%3A+%5C%225M%5C%22%2C+%5C%22idle_cost_ratio%5C%22%3A+0.3%7D%2C+%5C%22orders%5C%22%3A+%5B%7B%5C%22status%5C%22%3A+%5C%22preparing%5C%22%2C+%5C%22delivery%5C%22%3A+%7B%5C%22duration%5C%22%3A+%5C%220M%5C%22%2C+%5C%22ready_time%5C%22%3A+%5C%222021-04-07T13%3A05%3A04%2B10%3A00%5C%22%2C+%5C%22due_time%5C%22%3A+%5C%222021-04-07T13%3A09%3A04%2B10%3A00%5C%22%2C+%5C%22geo%5C%22%3A+%5C%22144.960489%2C-37.808585%5C%22%7D%2C+%5C%22order_id%5C%22%3A+%5C%2211022042%5C%22%2C+%5C%22ban_plate%5C%22%3A+%5B%5D%2C+%5C%22assigned%5C%22%3A+%5C%22%5C%22%2C+%5C%22pickup%5C%22%3A+%7B%5C%22duration%5C%22%3A+%5C%220M%5C%22%2C+%5C%22ready_time%5C%22%3A+%5C%222021-04-07T12%3A55%3A04%2B10%3A00%5C%22%2C+%5C%22due_time%5C%22%3A+%5C%222021-04-07T12%3A57%3A04%2B10%3A00%5C%22%2C+%5C%22geo%5C%22%3A+%5C%22144.96168%2C-37.808028%5C%22%7D%7D%5D%7D%2C+%5C%22config%5C%22%3A+%7B%5C%22max_iteration_num%5C%22%3A+500%2C+%5C%22use_estimated_distance%5C%22%3A+true%7D%7D%22%2C+%22bizId%22%3A+%22new-easi-vrp-1.5%22%2C+%22taskType%22%3A+1%7D%2C+%22requestId%22%3A+%2208ca1310974911eb9bcd06ebd4b32378%22%7D&msg_id=08ca3f3e974911eb9bcd06ebd4b32378&logistic_provider_id=wuLiuYun&to_code=greedSolver&data_digest=23fahiqu3yf%3D%3D'
r = requests.post('http://link.cainiao.com/gateway/link.do', data=para, headers=header, timeout=10.000)
print(r.content)