import dbutils.pooled_db
import pymysql


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

def fetch_one(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def fetch_all(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    user = cursor.fetchall()
    cursor.close()
    conn.close()
    return user

def insert(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.lastrowid # 用来拿到 刚刚 INSERT 进去的那条记录的自增主键 ID。 update等其他无效，可能返回0.