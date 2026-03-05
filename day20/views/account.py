import dbutils.pooled_db
import pymysql
from flask import Blueprint, render_template, request,redirect
"""
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Chen061215!LX",
    database="day21_project1",
    charset="utf8mb4"
)"""
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
    database="day21_project1",
    charset="utf8mb4",
)



#蓝图对象
ac = Blueprint('account', __name__)



@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    role = request.form.get('role')
    mobile = request.form.get('mobile')
    password = request.form.get('pwd')
    print(role,mobile,password)

#connect to MYSQL to check if the user is in the database
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute("select * from user_database where role=%s and mobile=%s and password=%s",(role,mobile,password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return redirect("/order/list") #跳转其他网址
    else:
        return render_template("login.html",error="登陆失败，请重试")





    return "good"



@ac.route('/users')
def users():
    return "用户列表"