# from flask import Flask, request
# import requests,json
#
# x = "4591cf16-f2a9-4126-936e-6d71155eae76"
#
# url = f"http://127.0.0.1:5000/task?ordered_string={x}"      #url
#
# datas = {
#      "ordered_string": "hello123","age2": "202" }
# # post数据，相当于客户在前端输入年纪和密码，然后发送到url
#
# #r = requests.get(url)
# #r = r.json()
# #print(r.json())
# #print(r.status_code)
# #print(r.headers)
#
# #print(r)     #返回 该路线返回的值。比如我写了return “true”。则打印true
#
#
# r1 = requests.post(url, json=datas)
# #r1 = r1.json()
# print(r1)
# #print(r.status_code)
# #print(r.headers)
#
# #print(r1,type(r1))     #返回 该路线返回的值。比如我写了return “true”。则打印true
#
import requests, json

url = "http://127.0.0.1:5000/task"

datas = {
    "ordered_string": "hello123",
    "age2": "202"
}

r1 = requests.post(url, json=datas)

print("status_code:", r1.status_code)
print("raw text:", repr(r1.text))


print(r1)  # 输出 Flask 返回的 JSON























