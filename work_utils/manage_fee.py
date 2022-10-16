# 管理费计算逻辑
# # # -*- coding: utf-8 -*-
# def calc_courier_manage_fee(order, courier, odb):
#     manage_fee = 0
#     if int(order.shop_id) in constants.GOMART_SHPOP_ID_LIST:
#         # gomart 商家管理费为0
#         current_app.logger.info(
#             "1-> calc_courier_manage_fee => shop_id in constants.GOMART_SHPOP_ID_LIST shop.id={}".format(
#                 order.shop_id))
#         return manage_fee
#     if courier is None:
#         current_app.logger.info("  * calc_courier_manage_fee calc_courier_manage_fee => courier is None")
#         return manage_fee
#
#     courier_ext = CourierExt.query.filter(CourierExt.courier_id == courier.id).first()
#     if courier_ext is None:
#         current_app.logger.info("* calc_courier_manage_fee calc_courier_manage_fee => courier_ext is None")
#         return manage_fee
#
#     # domino商家订单配送员佣金为0
#     if order.delivery_method == constants.SHOP_BUSINESS_DELIVERY_METHOD_SHOP and courier_ext.custom_manage_fee == 0 \
#             and courier_ext.custom_manage_fee_ratio == 0:
#         current_app.logger.info(
#             "2-> calc_courier_manage_fee => delivery_method == constants.SHOP_BUSINESS_DELIVERY_METHOD_SHOP and courier.custom_manage_fee == 0 and courier.custom_manage_fee_ratio == 0")
#         return manage_fee
#
#     if courier_ext.custom_manage_fee_ratio > 0:
#         if order.city_id == 3:
#             current_app.logger.info(
#                 "3->  calc_courier_manage_fee courier.custom_manage_fee_ratio={} > 0 order.city_id == 3".format(
#                     courier_ext.custom_manage_fee_ratio))
#             manage_fee = 0
#         elif order.city_id == 4:
#             current_app.logger.info(
#                 "4->  calc_courier_manage_fee courier.custom_manage_fee_ratio={} > 0 order.city_id == 4".format(
#                     courier_ext.custom_manage_fee_ratio))
#             manage_fee = 0
#         else:
#             manage_fee = float(odb.courier_delivery_fee) * courier_ext.custom_manage_fee_ratio
#             current_app.logger.info(
#                 "5-> calc_courier_manage_fee courier.custom_manage_fee_ratio={} > 0 order.city_id == {} odb.courier_delivery_fee={} courier_ext.custom_manage_fee_ratio = {} manage_fee={} ".format(
#                     courier_ext.custom_manage_fee_ratio,
#                     order.city_id, odb.courier_delivery_fee, courier_ext.custom_manage_fee_ratio, manage_fee))
#         return manage_fee
#
#     if order.city_id == 1:
#         if order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:  # 第三方商家订单不收取管理费
#             manage_fee = 0
#
#             current_app.logger.info(
#                 "6-> calc_courier_manage_fee order.city_id == 1 order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY manage_fee={}".format(
#                     manage_fee))
#         elif order.shop_type == constants.SHOP_TYPE_DELIVERY_SERVICE or order.shop_name.find(u'代购') > -1:
#             # 墨尔本系列私人配送和代购配送员管理费10%
#             manage_fee = float(odb.courier_delivery_fee) * 0.1
#
#             current_app.logger.info(
#                 "7-> calc_courier_manage_fee order.city_id == 1 order.shop_type == 3 order.shop_name={} odb.courier_delivery_fee={} manage_fee={}".format(
#                     order.shop_name, odb.courier_delivery_fee, manage_fee))
#         else:
#             if courier.create_time < '2018.05.01 06:00:00':
#                 courier_manage_fee = courier_ext.custom_manage_fee if courier else 0
#                 manage_fee_setting = SettingService.get_setting_value_with_key(
#                     constants.SETTING_MELBSC_DELIVERY_MANAGE_FEE)
#                 manage_fee = float(courier_manage_fee if courier_manage_fee > 0 else manage_fee_setting)
#                 current_app.logger.info(
#                     "8-> calc_courier_manage_fee order.city_id == 1 order.shop_type == {} order.shop_name={} courier.create_time={} courier_manage_fee={} manage_fee_setting={} manage_fee={}".format(
#                         order.shop_type, order.shop_name, courier_ext.create_time, courier_manage_fee,
#                         manage_fee_setting, manage_fee))
#             else:
#                 if courier.information_is_complete:
#                     courier_manage_fee = courier_ext.custom_manage_fee if courier_ext else 0
#                     manage_fee_setting = SettingService.get_setting_value_with_key(
#                         constants.SETTING_MELBSC_DELIVERY_MANAGE_FEE)
#                     manage_fee = float(courier_manage_fee if courier_manage_fee > 0 else manage_fee_setting)
#                     current_app.logger.info(
#                         "9-> calc_courier_manage_fee order.city_id == 1 order.shop_type == {} courier.information_is_complete= False order.shop_name={} courier.create_time={} courier_manage_fee={} manage_fee_setting={} manage_fee={}".format(
#                             order.shop_type, order.shop_name, courier_ext.create_time, courier_manage_fee,
#                             manage_fee_setting, manage_fee))
#                 else:
#                     # 管理费收配送费的10%
#                     manage_fee = float(odb.courier_delivery_fee) * 0.1
#                     current_app.logger.info(
#                         "10-> calc_courier_manage_fee order.city_id == 1 order.shop_type == {} courier.information_is_complete= True odb.courier_delivery_fee={} manage_fee={}".format(
#                             order.shop_type, odb.courier_delivery_fee, manage_fee))
#     elif order.city_id == 2:
#         if order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:  # 第三方商家订单不收取管理费
#             manage_fee = 0
#             current_app.logger.info(
#                 "11-> calc_courier_manage_fee order.city_id == 2 order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY")
#
#         elif order.shop_type == constants.SHOP_TYPE_DELIVERY_SERVICE or order.shop_name.find(u'代购') > -1:
#             # 墨尔本系列私人配送和代购配送员管理费10%
#             manage_fee = float(odb.courier_delivery_fee) * 0.1
#             current_app.logger.info(
#                 "12-> calc_courier_manage_fee order.city_id == 2 order.shop_type == constants.SHOP_TYPE_DELIVERY_SERVICE order.shop_name={} manage_fee={}".format(
#                     order.shop_name, manage_fee))
#         else:
#             # courier = Courier.query.get(order.courier_id)
#             courier_manage_fee = courier_ext.custom_manage_fee if courier else 0
#             manage_fee_setting = SettingService.get_setting_value_with_key(constants.SETTING_SYDSC_DELIVERY_MANAGE_FEE)
#             manage_fee = float(courier_manage_fee if courier_manage_fee > 0 else manage_fee_setting)
#             current_app.logger.info(
#                 "13-> calc_courier_manage_fee order.city_id == 2 order.shop_type == {} order.shop_name={} courier.create_time={} courier_manage_fee={} manage_fee_setting={} manage_fee={}".format(
#                     order.shop_type, order.shop_name, courier_ext.create_time, courier_manage_fee, manage_fee_setting,
#                     manage_fee))
#
#     elif order.city_id == 3:
#         # if order.shop_type == constants.SHOP_TYPE_DELIVERY_SERVICE:
#         #     manage_fee = 0  # 布里斯班私人配送，公司收4刀管理费
#         # elif order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:
#         #     manage_fee = 0  # 布里斯班第三方配送，公司收3刀管理费
#         # else:
#         #     # 管理费收配送费的10%
#         #     # manage_fee = float(odb.courier_delivery_fee) * 0.1
#         #     # 布里斯班管理费0
#         #     manage_fee = 0
#         #     # 特殊送餐员加收0.5元费用
#         #     # if courier and courier.display_name.find(u'全-EA') >= 0:
#         #     #     manage_fee += 0.5
#         manage_fee = 0
#         current_app.logger.info(
#             "16-> calc_courier_manage_fee order.city_id == 3 order.shop_type == {}".format(order.shop_type))
#     elif order.city_id == 4:
#         if order.shop_type == constants.SHOP_TYPE_DELIVERY_SERVICE:
#             manage_fee = 0  # 取消阿德莱德私人配送，公司收4刀管理费
#         elif order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:
#             manage_fee = 0  # 阿德莱德第三方配送，公司收3刀管理费
#         else:
#             # 管理费收配送费的10%
#             manage_fee = 0
#         current_app.logger.info(
#             "19-> calc_courier_manage_fee order.city_id == 4 order.shop_type == {}".format(order.shop_type))
#     elif order.city_id == 5:
#         if order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:
#             manage_fee = 0
#             current_app.logger.info(
#                 "20-> calc_courier_manage_fee order.city_id == 5 order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY")
#         else:
#             # # courier = Courier.query.get(order.courier_id)
#             # courier_manage_fee = courier_ext.custom_manage_fee if courier else 0
#             # manage_fee_setting = SettingService.get_setting_value_with_key(constants.SETTING_PERSC_DELIVERY_MANAGE_FEE)
#             # manage_fee = float(courier_manage_fee if courier_manage_fee > 0 else manage_fee_setting)
#             courier_manage_fee = courier_ext.custom_manage_fee if courier else 0
#             manage_fee_setting = SettingService.get_setting_value_with_key(constants.SETTING_PERSC_DELIVERY_MANAGE_FEE)
#             manage_fee = float(courier_manage_fee if courier_manage_fee > 0 else manage_fee_setting)
#             current_app.logger.info(
#                 "21-> calc_courier_manage_fee order.city_id == 5 courier_manage_fee={} manage_fee_setting={} manage_fee={}".format(
#                     courier_manage_fee, manage_fee_setting, manage_fee))
#     elif order.city_id == 7:
#         if order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:
#             manage_fee = 0
#             current_app.logger.info(
#                 "22-> calc_courier_manage_fee order.city_id == 7 order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY")
#         else:
#             # # 管理费收配送费的20%
#             # manage_fee = float(odb.courier_delivery_fee) * 0.2
#
#             # 管理费收配送费的20%
#             manage_fee = float(odb.courier_delivery_fee) * 0.2
#         current_app.logger.info(
#             "23-> calc_courier_manage_fee order.city_id == 7 order.shop_type == {} manage_fee={} odb.courier_delivery_fee={}".format(
#                 order.shop_type, manage_fee, odb.courier_delivery_fee))
#     elif order.city_id == 8:
#         # if order.shop_type == constants.SHOP_TYPE_ONLY_DELIVERY:
#         #     manage_fee = 0
#         # else:
#         #     # 管理费收配送费的10%
#         #     manage_fee = float(odb.courier_delivery_fee) * 0.1
#
#         # 管理费收配送费的10%
#         manage_fee = 0  # float(odb.courier_delivery_fee) * 0.1
#         current_app.logger.info(
#             "25-> calc_courier_manage_fee order.city_id == 8 order.shop_type == {} manage_fee={} odb.courier_delivery_fee={}".format(
#                 order.shop_type, manage_fee, odb.courier_delivery_fee))
#     return manage_fee
