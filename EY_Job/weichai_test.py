# -*- coding: utf-8 -*-
import pandas as pd

# 定义字段映射表
columns_map = {
    "标题": "功能点",
    "所属分组": "系统模块",
    "状态": "",
    "执行者": "编写作者",
    "前置条件": "前置条件",
    "步骤描述": "测试步骤",
    "预期结果": "预期结果",
    "实际结果": "",
    "用例类型": "类型",
    "用例等级": "重要程度",
    "标签": "",
}

df_a = pd.read_csv("产品销项发票测试用例.csv")

df_a.rename(columns=columns_map, inplace=True)

# 打开测试用例B的Excel文件
df_b = pd.read_excel("测试管理导入模板.xlsx")
# 筛选出表A和表B共同存在的列
common_columns = [col for col in df_a.columns if col in df_b.columns]
# print(common_columns)
# 使用concat将两个DataFrame合并
result_df = pd.concat([df_b, df_a[common_columns]], ignore_index=True)
result_df["重要程度"].replace({
    "P1": "最高",
    "P2": "较高",
    "P3": "普通",
    "P4": "较低",
    "P5": "最低",
}, inplace=True)

result_df["编写作者"] = "刘桐伸"
result_df["类型"] = "测试用例"

# 将结果写入新的Excel文件或覆盖现有文件
result_df.to_excel("result.xlsx", index=False)
