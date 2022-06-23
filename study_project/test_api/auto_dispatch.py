# -*- coding: utf-8 -*-
from study_project.test_api.courier import Courier
from study_project.test_api.order import Order
from study_project.test_api.test_public import Job

class AutoDispatch(object):
    @staticmethod
    def auto_dispatch(orders=[],couriers=[]):
        """
        1. 公有函数 自动分单 入参（骑手对象数组，订单对象数组） （目前只找一轮）
        1. 找到对于每个订单来说最近的那个骑手(最近指的是订单的商家距离到骑手距离最近），并且满足以下条件则直接分配订单
        1. 骑手在线
        2. 未完成订单数小于当前配置的背包对象
        3. 骑手距离商家距离小于5000米  
        3. 骑手类型等于delivery （ps上面三点注意和其他代码复用）
        1.订单的商家标签id为1可以分配给骑手标签为1或者2或者3的骑手
        2.商家标签id为2的可以分配给骑手id为3252
        3.商家标签为空的可以分配给所有骑手（该限制只有自动分单限制）
        5. 满足以上条件，则调用接单，并且后续该订单不参与其他骑手的分配（todo 需要思考）
        :param orders: 订单数组
        :param couriers: 骑手数组
        :return:
        """
        for order in orders:
            min_dis = 5000
            min_courier = None
            for courier in couriers:
                if courier.isable_get_order(order) == True:
                    # 单的商家标签id为1可以分配给骑手标签为1或者2或者3的骑手
                    if (order.shop_tag_id == 1 and courier.courier_tag_id in (1, 2, 3)) \
                            or (order.shop_tag_id == 2 and courier.courier_id == 3252) \
                            or (order.shop_tag_id is None):
                        # 这里找到对于每个订单来说最近的那个骑手(最近指的是订单的商家距离到骑手距离最近）
                        dis1 = order.shop_location.split(',')
                        dis2 = courier.courier_location.split(',')
                        temp = Job.distance_haversine_simple(dis1[0],dis1[1],dis2[0],dis2[1])
                        if temp < min_dis:
                            min_dis = temp
                            min_courier = courier
                else:
                    continue
            if min_courier is not None:
                min_courier.get_order(user_location=order.user_location,order=order)


courier = Courier(courier_location='131.2222,1.444', couier_package=3, courier_tag_id=[1])
print(courier)
order = Order(user_location='131.4547,1.474', shop_location='131.9999,1.999', shop_tag_id=[1])
print(order)






