"""基于文件(.txt)进行授权（是否在数据中）"""


#————————————————————————————————————————————————————————————————————————————————————————

import requests
#负责你的 Python → 别人的 API / 网站
import time
from flask import Flask, request, jsonify
import json
import hashlib   #------ 哈希加密库


#request 第三方库- 负责收数据，如url等
#Ex:http://127.0.0.1:5000/xxx
#http://127.0.0.1:5000/xxx?age=19&pwd=123


app = Flask(__name__)

def get_user_dict():
    intfo_dict = {}
    with open("test.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            token, name = line.split(",")
            intfo_dict[name] = token
    return intfo_dict



@app.route("/xxx",methods=["GET","POST"])
def index():
    """
    请求的URL需要携带： http://127.0.0.1:5000/xxx?token=829a156f-d218-4d4a-9021-5f4fe923daa1
    :return:
    """
    token = request.args.get('token')     #基于URL
    user_dirt = get_user_dict()

    if not token:
        return jsonify({"status" : False, "error" : "ERROR"})
    if token in user_dirt:
        return jsonify({"status" : True, "data" : user_dirt[token]})


@app.route("/yyy")
def home():
    return "false"


if __name__ == "__main__":
    # import uuid
    #
    # uid = uuid.uuid4()
    # print(uid)

    app.run()


