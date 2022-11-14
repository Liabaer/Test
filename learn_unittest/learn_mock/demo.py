import requests


def send_request(url):
    r = requests.get(url)
    return r.status_code

def visit_baidu():
    url = "http://baidu.com"
    return send_request(url)