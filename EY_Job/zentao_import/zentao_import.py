# -*- coding: utf-8 -*-
import hashlib
import pandas as pd
import requests
from torch.onnx._internal.diagnostics.infra.sarif import Tool
import json


def create_user_excel(demo):
    '''
    将用户数据写入excel
    :param demo:
    :return:
    '''
    if demo[-1] == ";":
        data = demo[:-1].split(";")
    else:
        data = demo.split(";")
    df = pd.DataFrame({
        "登陆账号": [item.split("<")[0].replace(" ", "") for item in data],
        # "account": [item.split("<")[1].split(">")[0].replace(" ", "") for item in data],
        "登陆密码": "Aa123456"
    })
    df.to_excel("禅道用户.xlsx", index=False)
    return


demo = "Kathy Cheuk <Kathy.Cheuk@hk.ey.com>; Justin CH Chan <Justin.CH.Chan@hk.ey.com>;Paul Yeung <Paul.Yeung@hk.ey.com>;coco<coco.lau@hk.ey.com>; sandy<sandy.hy.lau@hk.ey.com>;Kaylee Tong <Kaylee.Tong@cn.ey.com>;Peter YH Li <Peter.YH.Li@cn.ey.com>;Ivy ZM Mo <Ivy.ZM.Mo@cn.ey.com>;Patrick YF Deng <Patrick.YF.Deng@cn.ey.com>;Ivy CW Li <Ivy.CW.Li@cn.ey.com>;Yonnie Chen <Yonnie.Chen@cn.ey.com>;Blair Chen <Blair.Chen@cn.ey.com>;Mark Liang <Mark.Liang@cn.ey.com>;Matthew JY Li <Matthew.JY.Li@cn.ey.com>;Tessa Guo <Tessa.Guo@cn.ey.com>;Reese Xu <Reese.Xu@cn.ey.com>;"

df = pd.read_excel("禅道用户.xlsx")
create_user_excel(demo)


# available_rows = df.dropna(axis=1).shape[0]


# print(df)


def md5(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()


# print(md5('Aa123456'))


def update_payload_with_excel_data(df):
    """
    使用 Excel 数据更新 payload
    :param df: DataFrame 对象
    :return: 更新后的 payload
    """
    payload = {'userType': 'inside',
               'company[1]': '',
               'dept[1]': '0',
               'account[1]': 'tt1',
               'realname[1]': 'tt1',
               'visions[1][]': 'rnd',
               'role[1]': 'qa',
               'group[1][]': '3',
               'email[1]': '',
               'gender[1]': 'm',
               'password[1]': 'Aa123456789',
               'commiter[1]': '',
               'join[1]': '',
               'skype[1]': '',
               'qq[1]': '',
               'dingding[1]': '',
               'weixin[1]': '',
               'mobile[1]': '',
               'slack[1]': '',
               'whatsapp[1]': '',
               'phone[1]': '',
               'address[1]': '',
               'zipcode[1]': '',
               'verifyPassword': '41651126b2f8da035c15194a1de2cb24'}
    for row_index, row in df.iterrows():
        payload["account[{}]".format(row_index + 1)] = row["account"]
        payload["realname[{}]".format(row_index + 1)] = row["realname"]
        payload["company[{}]".format(row_index + 1)] = ''
        payload["dept[{}]".format(row_index + 1)] = '0'
        payload["visions[{}]".format(row_index + 1)] = 'rnd'
        payload["role[{}]".format(row_index + 1)] = 'qa'
        payload["group[{}]".format(row_index + 1)] = '3'
        payload["email[{}]".format(row_index + 1)] = ''
        payload["gender[{}]".format(row_index + 1)] = 'm'
        payload["password[{}]".format(row_index + 1)] = 'Aa123456789'
        payload["commiter[{}]".format(row_index + 1)] = ''
        payload["join[{}]".format(row_index + 1)] = ''
        payload["skype[{}]".format(row_index + 1)] = ''
        payload["qq[{}]".format(row_index + 1)] = ''
        payload["dingding[{}]".format(row_index + 1)] = ''
        payload["weixin[{}]".format(row_index + 1)] = ''
        payload["mobile[{}]".format(row_index + 1)] = ''
        payload["slack[{}]".format(row_index + 1)] = ''
        payload["whatsapp[{}]".format(row_index + 1)] = ''
        payload["phone[{}]".format(row_index + 1)] = ''
        payload["address[{}]".format(row_index + 1)] = ''
        payload["zipcode[{}]".format(row_index + 1)] = ''
    return payload


updated_payload = update_payload_with_excel_data(df)

# print(updated_payload)

url = "https://zentao.ey.com.cn/zentao"
zentao_username = "tul"
zentao_password = "Aa123456"


def gain_session():
    session = requests.Session()
    '''获取禅道sessionid'''
    session_url = url + "/api-getsessionid.json?m=api&f=getSessionID&t=json"
    re = session.get(session_url, verify=False)
    if re.status_code == 200:
        reslut = json.loads(re.text)
        data = reslut['data']
        data_dic = json.loads(data)
        session_name = data_dic['sessionName']
        session_id = data_dic['sessionID']
        return session, session_name, session_id


def get_headers():
    session, sessionName, sessionID = gain_session()
    '''用户登陆'''
    login_url = url + "/user-login.json"
    re = session.post(login_url + "?" + sessionName + "=" + sessionID,
                      data={"account": zentao_username, "password": zentao_password}, verify=False)
    # print(re.text)
    header = {'Cookie': 'sessionID' + sessionID}
    return session


def batch_user_import(payload):
    '''批量导入禅道用户'''
    batch_url = "https://zentao.ey.com.cn/zentao/user-batchCreate-0.json"
    session = get_headers()
    headers = {'Referer': 'https://zentao.ey.com.cn/zentao/user-batchCreate-0.html'}
    re = session.post(batch_url, payload, headers=headers,
                      files={}, verify=False)
    return re.content

# print(updated_payload)
# result = batch_user_import(payload=updated_payload)
# print(result)

#
# def add_user():
#     # 请求参数
#     params = {
#         "dept": 1,
#         "account": "Jack10",
#         "password1": "123456",
#         "password2": "123456",
#         "realname": "Jack10",
#         "join": "2019-11-11",
#         "role": "dev",
#         "group": 2,
#         "email": "jack2019@gmail.com",
#         "commiter": "http://jack2019.com",
#         "gender": "m"
#     }
#
#     # 调用 addUser 方法
#     result = add_user(params)
#
#     # 返回结果
#     return result

# sid = get_headers().get('Cookie')
# url = "https://zentao.ey.com.cn/zentao/search-buildQuery.html"
# payload = 'fieldrealname=&fieldemail=&fielddept=&fieldaccount=&fieldrole=&fieldphone=&fieldjoin=&fieldvisions=rnd&fieldid=&fieldcommiter=0&fieldgender=m&fieldqq=&fieldskype=&fielddingding=&fieldweixin=&fieldslack=&fieldwhatsapp=&fieldaddress=&fieldzipcode=&andOr1=AND&field1=realname&operator1=include&value1=a&andOr2=and&field2=email&operator2=include&value2=&andOr3=and&field3=dept&operator3=belong&value3=&groupAndOr=and&andOr4=AND&field4=account&operator4=include&value4=&andOr5=and&field5=role&operator5=%3D&value5=&andOr6=and&field6=phone&operator6=include&value6=&module=user&actionURL=%2Fzentao%2Fcompany-browse-all-myQueryID-bysearch.html&groupItems=3&formType=lite'
# headers = {
#     'authority': 'zentao.ey.com.cn',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
#     'cache-control': 'no-cache',
#     'content-type': 'application/x-www-form-urlencoded',
#     'cookie': f'lang=zh-cn; device=desktop; theme=default; zentaosid={sid}; bugBranch=0; treeBranch=all; qaBugOrder=id_desc; bugModule=0; lastBugModule=0; pagerBugBrowse=100; preProductID=28; downloading=1; preBranch=0; tab=admin; goback=%7B%22qa%22%3A%22https%3A%5C%2F%5C%2Fzentao.ey.com.cn%5C%2Fzentao%5C%2Fbug-browse-28-all-unresolved.html%22%2C%22execution%22%3A%22https%3A%5C%2F%5C%2Fzentao.ey.com.cn%5C%2Fzentao%5C%2Fproject-browse.html%22%2C%22admin%22%3A%22https%3A%5C%2F%5C%2Fzentao.ey.com.cn%5C%2Fzentao%5C%2Fcompany-browse-all-myQueryID-bysearch.html%22%7D; selfClose=1; windowWidth=1690; windowHeight=434; lang=zh-cn; device=desktop; theme=default',
#     'origin': 'https://zentao.ey.com.cn',
#     'pragma': 'no-cache',
#     'referer': 'https://zentao.ey.com.cn/zentao/company-browse-all-myQueryID-bysearch.html',
#     'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'iframe',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
