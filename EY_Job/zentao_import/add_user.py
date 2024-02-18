# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import re

zentao_url = "https://zentao.ey.com.cn/zentao/api.php/v1"
admin_username = "tul"
admin_password = "Aa123456"
# 这里直接放入需要添加的用户名单

demo = "coco<coco.lau@hk.ey.com>; sandy<sandy.hy.lau@hk.ey.com>;Kaylee Tong <Kaylee.Tong@cn.ey.com>;Peter YH Li <Peter.YH.Li@cn.ey.com>;Ivy ZM Mo <Ivy.ZM.Mo@cn.ey.com>;Patrick YF Deng <Patrick.YF.Deng@cn.ey.com>;Ivy CW Li <Ivy.CW.Li@cn.ey.com>;Yonnie Chen <Yonnie.Chen@cn.ey.com>;Blair Chen <Blair.Chen@cn.ey.com>;Mark Liang <Mark.Liang@cn.ey.com>;Matthew JY Li <Matthew.JY.Li@cn.ey.com>;Tessa Guo <Tessa.Guo@cn.ey.com>;Reese Xu <Reese.Xu@cn.ey.com>;"


class AddZentaoUser(object):

    def __init__(self, username, pwd, url):
        self.username = username
        self.pwd = pwd
        self.url = url
        self.session = requests.Session()

    # 获取token
    def get_cookie(self):
        url = f"{self.url}/tokens"
        res = self.session.post(url, json={"account": self.username, "password": self.pwd})
        token = ""
        try:
            token = res.json().get("token")
        except Exception as error:
            print(f"获取cookie失败: {error}; 内容: {res.content}")
        return token

    def create_payload_bystring(self, data):
        """
        如果提供的是字符串 使用这个函数处理用户数据
        记得group字段每次根据提供的部门传入修改添加的用户权限
        :param data: 提供的字符串
        :return:
        """
        results = []
        data.replace('；', ';')
        if data[-1] == ";":
            users = data[:-1].split(";")
        else:
            users = data.split(";")
        for user in users:
            account, realname = user.split("<")[0].replace(".", ""), user.split("<")[1][:-1]
            result = {"realname": realname, "account": account.replace(" ", ""), "password": "Aa123456", 'rule': "qa",
                      'group': "3"}
            results.append(result)
        payload = json.dumps(results)
        return payload

    def create_payload_byexcel(self, filename, email):
        """
        如果给的是excel，使用这个这个函数处理数据
        记得group字段每次根据提供的部门传入修改添加的用户权限
        :param filename: 提供的excel文件名
        :param email: 包含email的列
        :return:
        """
        df = pd.read_excel(filename, usecols=[email])
        df.dropna(inplace=True)
        df[email] = df[email].fillna(0).astype(str)
        str = ''
        results = []
        for i in df[email]:
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
        # print(payload)
        return payload

    # 添加用户
    def add_user(self, paylaod):
        url = f"{self.url}/users"
        header = {"Token": self.get_cookie()}
        res = self.session.post(url, json=paylaod, headers=header)
        data = {}
        try:
            data = res.json()
            if data.get("error"):
                print(data.get("error"))
        except Exception as error:
            print(f"创建用户失败: {error}; res content: {res.content}")
        return data

    def create_user_excel(demo):
        '''
        将用户数据回写入excel给用户
        :param demo:将处理后的payload数据传入
        :return:
        '''
        if demo[-1] == ";":
            data = demo[:-1].split(";")
        else:
            data = demo.split(";")
        df = pd.DataFrame({
            "登陆账号": [item.split("<")[0].replace(" ", "") for item in data],
            "登陆密码": "Aa123456"
        })
        df.to_excel("禅道用户.xlsx", index=False)
        return


adduser = AddZentaoUser(url=zentao_url, username=admin_username, pwd=admin_password)
print(adduser.create_payload_bystring(demo))

# 将写入的数据写入Excel


# 如果提供的是string，直接处理
users = adduser.create_payload_bystring(demo)
# # 如果提供的是excel
# users = adduser.create_payload_byexcel('user.xlsx', 'Email')
#
# adduser.create_user_excel(users)


# 循环调用方法添加用户
for user in json.loads(users):
    # print(user)
    adduser.add_user(user)
