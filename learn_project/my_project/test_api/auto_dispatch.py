# -*- coding: utf-8 -*-
from learn_project.my_project.test_api.courier import Courier
from learn_project.my_project.test_api.courier_package import CourierPackage
from learn_project.my_project.test_api.order import Order
from learn_project.my_project.test_api.test_public import Job


class AutoDispatch(object):
    @staticmethod
    def auto_dispatch(orders=[], couriers=[]):
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
                print('000')
                flag = False
                if courier.isable_get_order(order) == True:
                    # 单的商家标签id为1可以分配给骑手标签为1或者2或者3的骑手
                    if 1 in order.shop_tag_id and set(courier.courier_tag_id) & {1, 2, 3}:
                        print('111', min_courier)
                        flag = True
                    if 2 in order.shop_tag_id and courier.courier_id == 3252:
                        print('222', min_courier)
                        flag = True
                    if (order.shop_tag_id is None):
                        print('333', min_courier)
                        flag = True
                    if flag:
                        # 这里找到对于每个订单来说最近的那个骑手(最近指的是订单的商家距离到骑手距离最近）
                        dis1 = order.shop_location.split(',')
                        dis2 = courier.courier_location.split(',')
                        temp = Job.distance_haversine_simple(dis1[0], dis1[1], dis2[0], dis2[1])
                        if temp < min_dis:
                            min_dis = temp
                            min_courier = courier

                else:
                    continue

            if min_courier is not None:
                min_courier.get_order(user_location=order.user_location, order=order)
                print('骑手id:' + min_courier.courier_id + '接单中')
            else:
                print('当前订单id:' + order.order_id + '未找到骑手')


# courier_package = CourierPackage(package_name='测试背包',package_param={1:3,2:4})
# courier = Courier(courier_location='131.3333,1.2222', courier_package=courier_package, courier_tag_id=[1])
# # print(courier)
# order = Order(user_location='131.4547,1.474', shop_location='131.9999,1.999', shop_tag_id=[1], email=['Rena0401@gmail.com'])
# # print(order)
#
# 测试接单
# courier.update_status()
# print(courier.isable_get_order(order))
# courier.get_order(user_location='131.3333,1.2222', order=order)
# print('订单配送费：'+str(order.delivery_fee), '订单状态：'+order.order_status)
# courier.completed_order(order)
# print('订单配送费'+str(order.delivery_fee), '订单状态'+order.order_status)

courier_package = CourierPackage(package_name='测试背包', package_param={1: 2, 2: 4})
courier_a = Courier(courier_location="1.3020385,103.8803897", courier_package=courier_package, courier_tag_id=[1])
courier_b = Courier(courier_location='131.322,1.233', courier_package=courier_package, courier_tag_id=[1])
order_a = Order(user_location="1.3020475,103.8803537", shop_location="1.3020375,103.8803837", shop_tag_id=[1],
                email=['Rena0401@gmail.com'])
order_b = Order(user_location="1.3020475,103.8803837", shop_location="1.3020475,103.8803837", shop_tag_id=[1],
                email=['Rena401@gmail.com'])
order_c = Order(user_location="1.3120675,103.8803837", shop_location="1.3120475,103.8803437", shop_tag_id=[1],
                email=['Rena0401@gmail.com'])
order_d = Order(user_location="1.3120275,103.8803437", shop_location="1.3120275,103.8803337", shop_tag_id=[1],
                email=['Rena0401@gmail.com'])

courier_b.update_status()
courier_a.update_status()
AutoDispatch.auto_dispatch(orders=[order_a, order_b, order_c, order_d], couriers=[courier_a, courier_b])
