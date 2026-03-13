"""基于文数据库（MySQL）进行授权（是否在数据中）"""


#——————————————————————————————————————————————————————————————————————————————————————
import pymysql,json,requests,time
from flask import Flask, request, jsonify



conn = pymysql.connect(         #connect to mysql
    host="localhost",
    user="root",
    password="Chen061215!LX",
    database="flask_test",
    charset="utf8mb4"

)
flask = Flask(__name__)

def get_user_dict(token):
    cursor = conn.cursor() # conn 创建游标对象，连接对象
    cursor.execute("select * from infor") #执行
    result = cursor.fetchall() #一次拿所有条数据
    #fetchmany(n)       -一次拿n条数据
    #fetchone()         -一次拿1条数据
    for i in result:
        if i[2] == token:
            return True

    return False

@flask.route("/xxx",methods=["GET","POST"])
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




"""
import sqlite3

DB_PATH = "database.db"

def main():
    # 1. 连接数据库（没有就自动创建）
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("select * from users")
        result = cursor.fetchall()  # 一次拿所有条数据
        print(result)

        # 2. 创建表（如果不存在）
    #     cursor.execute(""
    #         CREATE TABLE IF NOT EXISTS users (
    #             id INTEGER PRIMARY KEY,
    #             name TEXT
    #         )
    #     "")
    #
    #     # 3. 插入一条数据（id = 0, name = owen）
    #     cursor.execute(""
    #         INSERT OR REPLACE INTO users (id, name)
    #         VALUES (?, ?)
    #     "", (0, "owen"))
    #
    #     # 4. 提交（with 会自动提交，这行写不写都行，写了更直观）
    #     conn.commit()
    #
    # print("SQLite 数据库已创建，并插入：id=0, name=owen")


#if __name__ == "__main__":
 #   main()



"""
