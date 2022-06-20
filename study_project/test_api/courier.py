# -*- coding: utf-8 -*-
# 1. 定义一个骑手类Courier
class Courier(object):

    # 1. 私有属性
    #     1. 骑手id
    #     2. 骑手经纬度（逗号分割 lng,lat)
    #     3. 骑手状态 （online，offline)
    #     4. 骑手未完成订单id列表 （订单id逗号分割）
    #     5. 骑手类型 （delivery,shop_deliver)
    def __init__(self, courier_id='', xy=[], status='', uncompleted_order_id=[], delivery_type=''):
        self.courier_id = id
        self.xy = []
        self.status = ''
        self.uncompleted_order_id = []
        self.delivery_type = ''

    # 1. 获取骑手经纬度
    def get_xy(self):
        return self.xy

    # 2. 修改骑手经纬度
    def update_xy(self):
        new_xy = []
        return new_xy

    # 3. 判断骑手是否在线
    def is_online(self):
        if self.status == 'online':
            return True
    # 4. 修改骑手状态（切换上下线）

    def update_status(self):
        if self.status == 'online':
            self.status = 'offline'
        if self.status == 'offline':
            self.status = 'online'
        return self.status

    # 4. 获取骑手未完成订单数

    def get_uncompleted_order_list(self):
        return self.uncompleted_order_id
    # 5. 接单函数（满足以下条件则接单）（传入参数用户经纬度，订单id）
#             1. 骑手状态等于online
#             2. 未完成订单数小于3
#             3. 距离用户小于3000米直线距离
#             4. 骑手类型等于delivery
#             5. 满足以上条件则接单，把新订单id，写入到骑手未完成列表中
#             6. 打印接单成功订单id：xxx, 否则打印接单失败，并且输出具体的失败原因（比如距离大于3000米）
#         6. 完成订单函数 （传入需要完成的订单id)
#             1. 骑手状态等于online
#             2. 如果未完成订单列表存在订单id
#             3. 满足以上条件则完成订单，并且将订单id从未完成列表中删除
#             4. 成功打印完成订单id:xxxx 否则打印完成订单失败（不存在该订单）
#     4. 公有函数
#         1. 计算2个经纬度之间的直线距离（输入2个经纬度 输出距离） 参考下方代码计算
