""" 从客户端请求获取JSON数据，返回的是一个字典。再通过哈希运算MD5创造sign"""

#-----------------------------------------------------------

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

@app.route("/xxx",methods=["GET","POST"])
def index():
    ordered_string = request.get_json()    #从客户端请求中获取 JSON 数据，返回的是一个字典
    newstring = ordered_string["ordered_string"]#保存ordered_string(key)的value
    if not ordered_string:
        return jsonify({"status" : False, "error": "ERROR"})#如果客户端没有传数据（ordered_string 为空），返回错误 JSON
    secret = "fuaiuehfebdai2173d" #加密用的固定秘密（salt），用于增强安全性
    encrypt_string  = newstring + secret #合并
    s = encrypt_string.encode('utf-8') #将字符串转换成字节（bytes），因为 hashlib.md5 只能处理字节
    obj = hashlib.md5(s) #对字节进行 MD5 哈希运算，得到一个 MD5 对象   ; 不可逆，所以无法解析，除非彩虹表（别人借好的去参考）或者暴力破解
    obj.update(b"xinneirong")
    sign = obj.hexdigest() #将 MD5 对象转换成十六进制字符串，作为最终签名（sign）
    return  jsonify({"status" : True, "data" : sign}) #返回






@app.route("/yyy")
def home():
    return "false"


if __name__ == "__main__":
    app.run()


