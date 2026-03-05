"""连接池通过复用数据库连接、避免频繁创建销毁的开销，是提升高并发场景下系统性能和稳定性的关键优化手段"""

#-----------------------------------------------------------------------------------------



import pymysql, json, requests, time
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


def get_user_dict(token):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select * from infor")
    result = cursor.fetchall()  # 一次拿所有条数据
    # fetchmany(n)       -一次拿n条数据
    # fetchone()         -一次拿1条数据
    for i in result:
        if i[2] == token:
            return True

    return False


@flask.route("/xxx", methods=["GET", "POST"])
def token():
    if request.method == "GET":
        token = request.args.get("token")
        result = get_user_dict(token)
        if result:
            return jsonify({"result": "Success"})
        else:
            return jsonify({"result": "Fail"})


if __name__ == "__main__":
    flask.run()
