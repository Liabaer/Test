import requests
# 测试自己编写的接口的返回数据


resp = requests.get("http://127.0.0.1:8080/test-get", params={"name": "yanxu", "age": 2})
print(resp.content)

resp = requests.post("http://127.0.0.1:8080/test-post", headers={'Content-Type': 'application/json'},
                     json={"name": "liabaer", "age": 1})
print(resp.content)

