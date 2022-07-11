from flask import Flask
from flask import request

# flask是一个python编写接口的框架

# 初始化flask
app = Flask(__name__)


# @app.route 第一个是接口的路径，第二个参数是支持的请求方法
# name和age是get请求的2个参数，可以用requests调用一下试试看，新建一个文件test_learn_api.py
@app.route('/test-get', methods=['GET'])
def test_get_method():
    # get的参数在args里面
    return {
        "data": {
            "name": request.args.get("name"),  # 获取 get请求的参数
            "age": request.args.get("age"),
        },
        "errorMessage": ""
    }


@app.route('/test-post', methods=['POST'])
def test_post_method():
    # post的参数在json里面
    return {
        "data": {
            "name": request.json.get("name"),
            "age": request.json.get("age")
        }
    }


# 运行后端服务，后端服务有以上接口，端口是8080，host是127.0.0.1,debug开启
app.run(host="127.0.0.1", port=8080, debug=True)

