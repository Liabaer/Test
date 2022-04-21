from openpyxl import Workbook
from allpairspy import AllPairs

# headers里面填对应的因素
headers = ["外卖类型", "本单是否享受B类用户减免", "优惠券类型", "配送类型", "当前大区是否存在会员配置", "订单金额是否门槛满足", "本单会员减免总金额"]
# parameters里面填写相关的水平
parameters = [
    ["外卖或者次日送达", "非外卖或者次日送达"],
    ["是", "否"],
    ["商家优惠券", "商家满减/满折", "配送费立减"],
    ["平台配送", "不是平台配送"],
    ["是", "否"],
    ["是", "否"],
    ["本单会员减免总金额大于0", "本单会员减免总金额等于0"]
]
sheet_name = "表名1"
wb = Workbook()
info_result = []
if len(headers):
    info_result.append(headers)

for i, pairs in enumerate(AllPairs(parameters)):
    info_result.append(pairs)
ws1 = wb.active
ws1.title = sheet_name  # sheet名称

print(info_result)
for row in info_result:
    ws1.append(row)
wb.save('确认下单会员购买卡片展示情况正价表格.xlsx')  # Excel文件名称，保存文件
