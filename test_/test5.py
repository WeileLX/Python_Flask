"""
连接池：解决的是“频繁与数据库建立连接太慢”的问题，让多个请求共用一批已建好的连接。

redis队列：解决的是“生产者太快、消费者太慢”的问题，让任务先存起来，避免丢失或阻塞。

!!!!!!!!!!!!!!!!!!
代码中并不想要写两个连接池和pymysql连接.一个就够
"""

#--------------------------------------------------------------------------


import pymysql, json, requests, time,uuid, redis
from flask import Flask, request, jsonify
#from dbutils.pooled_db import PooledDB
import dbutils.pooled_db
flask = Flask(__name__)


POOL = dbutils.pooled_db.PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=10,
    maxcached=10,
    blocking=True,
    setsession=[],
    ping=0,
    host="localhost",
    user="root",
    password="Chen061215!LX",
    database="flask_test",
    charset="utf8mb4"
#    maxusage=None,

)

conn = pymysql.connect(  # connect to mysql
    host="localhost",
    user="root",
    password="Chen061215!LX",
    database="flask_test",
    charset="utf8mb4"

)

@flask.route("/task",methods=["GET","POST"])
def task():
    if request.method == "POST":
        ordered_string = request.json.get("ordered_string")
        if not ordered_string:
            return jsonify({"result": "Fail"})
        tid = str(uuid.uuid4())
        info_dict = {'tid':tid,'data':ordered_string}
        redis_conn_params = redis.Redis(host='localhost', port=6379, decode_responses=True)

        redis_conn_params.lpush("spider_task_list",json.dumps(info_dict))
        return jsonify({"result": "True"})



if __name__ == "__main__":
    flask.run()
