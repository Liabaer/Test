import requests

from functools import cached_property

base_url = "https://zentao.ey.com.cn/zentao/api.php/v1"
base_username = "tul"
base_password = "Aa123456"


class ZenTaoService(object):

    def __init__(self, url, username, pwd):
        self.url = url
        self.username = username
        self.pwd = pwd
        self.session = requests.Session()

    # functools 是 Python 标准库中的模块，包含了一些用于函数操作的高阶函数。cached_property 是 functools 模块中的一个装饰器，它可以将一个普通的属性转换为一个缓存属性。
    # 缓存属性是指，当属性第一次被访问时，会计算其值并缓存到内存中。之后，再次访问该属性时，直接从缓存中获取值，而不会再次计算。
    @cached_property
    def get_token(self) -> str:
        url = f"{self.url}/tokens"
        if not self.username or not self.pwd:
            return ""
        res = self.session.post(url, json={"account": self.username, "password": self.pwd})
        token = ""
        try:
            token = res.json().get("token")
        except Exception as e:
            print(f"get token is error: {e}; res content: {res.content}")
        return token

    def add_use(self, username, pwd, rule, group, real_name="", gender=""):
        url = f"{self.url}/users"
        header = {"Token": self.get_token}
        req_data = {
            "account": username,
            "password": pwd,
            "realname": real_name,
            "rule": rule,
            "group": group,
            "gender": gender
        }
        res = self.session.post(url, json=req_data, headers=header)
        data = {}
        try:
            data = res.json()
            if data.get("error"):
                print(data.get("error"))
        except Exception as e:
            print(f"get token is error: {e}; res content: {res.content}")
        return data


zentao_service = ZenTaoService(base_url, base_username, base_password)
print(zentao_service.add_use("wznb2", "wznb123456", "qa", "3", real_name="伟总牛逼2"))
