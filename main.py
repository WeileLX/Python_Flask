import requests
#负责你的 Python → 别人的 API / 网站
import time
from flask import Flask, request, jsonify
import json

#request 第三方库- 负责收数据，如url等
#Ex:http://127.0.0.1:5000/xxx
#http://127.0.0.1:5000/xxx?age=19&pwd=123


app = Flask(__name__)


# 后端的“接口入口” ->       执行index             get请求
# 后端的“接口入口” ->       执行index             post请求 (用户输入)


# /xxx          ->       执行index             get请求
@app.route("/xxx",methods=["GET","POST"])
def index():

    data = {}

    if request.is_json:
#        data = request.json
        data = request.get_json()    #更规范，安全 可以传参：force=True（强制JSON解析）,silent=True(出错不报错，返回None)
        print(data,type(request.json))


        #return json.dumps(data)        #python   ->        字符串   写文件/大日志/存数据库/自己输出/ --- 不是专门给Flask返回用的
        return jsonify(data)          # python  ->        HTTP响应JSON
        #return data


    if request.method == "POST":
        age2 = request.form.get("age2")
        pwd2 = request.form.get("pwd2")
        return f"age2:{age2},pwd2:{pwd2}"

    if request.method == "GET":
        age = request.args.get("age")
        pwd = request.args.get("pwd")
        return f"age:{age},pwd:{pwd}"
    return "false"






@app.route("/yyy")
def home():
    return "false"


if __name__ == "__main__":
    app.run()


