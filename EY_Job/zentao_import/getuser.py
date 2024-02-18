# -*- coding: utf-8
import json
import re
import pandas as pd

df = pd.read_excel('user.xlsx', usecols=['Email'])
df.dropna(inplace=True)
df['Email'] = df['Email'].fillna(0).astype(str)
str = ''
results = []
for i in df['Email']:
    # str += i + ';'
    # print(i)

    if "<" not in i:
        # 定义原始字符串
        s = i
        # 使用正则表达式匹配 @ 前面的文本
        match = re.search(r'[^<]*@', s)
        if match:
            # 获取匹配到的文本
            text = match.group()[:-1]
            # 将原始字符串用 <> 包起来
            new_s = '<' + s + '>'
            # 输出结果
            # print(f'原始字符串：{s}')
            # print(f'新字符串：{new_s}')
            # print(f'@ 前面的文本：{text}')
        else:
            print('未找到匹配的文本')
        i = text + new_s
        print(i)
    account, realname = i.split("<")[0].replace(".", ""), i.split("<")[1][:-1]
    result = {"realname": realname, "account": account.replace(" ", ""), "password": "Aa123456", 'rule': "qa",
              'group': "3"}
    results.append(result)
payload = json.dumps(results)

print(payload)

#
# for r in result:
#     account, realname = r.split("<")[0].replace('\n', ''), r.split("<")[1][:-1].replace('\n', '')
#     payload = {"realname": realname, "account": account.replace(" ", ""), "password": "Aa123456", 'rule': "qa",
#                'group': "3"}
#
# # 输出结果
# print(payload)
