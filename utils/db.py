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
    cursor = conn.cursor()
    cursor.execute(sql,params)
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user