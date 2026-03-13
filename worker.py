import time
from concurrent.futures import ThreadPoolExecutor
import redis
import pymysql
import dbutils.pooled_db

DB_POOL = dbutils.pooled_db.PooledDB(
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

def db_update_order(sql,params):
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    conn.commit()
    cursor.close()
    conn.close()
    return cursor.lastrowid  # 用来拿到 刚刚 INSERT 进去的那条记录的自增主键 ID。 update等其他无效，可能返回0.

def fetch_one(sql,params):
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def fetch_all(sql,params):
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql,params)
    user = cursor.fetchall()
    cursor.close()
    conn.close()
    return user

REDIS_POOL = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True,max_connections=1000)

def pop_queue():
    conn = redis.Redis(connection_pool=REDIS_POOL)
    data = conn.brpop("DAY21_TASK_QUEUE",timeout=10)
    if not data:
        return
    #print(data)
    return data[1]

conn = redis.Redis(connection_pool=REDIS_POOL)

def fetch_total_queue():

#    total_count = conn.lrange("DAY21_TASK_QUEUE",0,-1)   #从列表里按下标范围取元素。 0 到 -1，
                                                            #是指全部。数据量太大可能崩溃，因为它直接取整个列表从redis
    cache_list = conn.lrange("DAY21_TASK_QUEUE",0,-1)
    cache_int_list = {int(x) for x in cache_list}
    return cache_int_list

#    conn.hscan_iter() # （hash的）自定义增量迭代。比如：每次取100，然后生成 生成器，然后返回给你后再取100。 原因：一次性获取大量数据可能导致程序崩溃

"""
1.数据库获取待执行的订单ID
2.去redis中获取待执行的订单ID
3.找到数据库中有且 redis队列种没用所有订单ID -> 重新放到redis队列中
：return;
"""
def db_queue_init():
    #1. 数据库待执行
    result_list = fetch_all("select * from order_database where status = 1",[])
    db_id_list={item['id'] for item in result_list}
    #print(db_id_list)
    #2. redis中待执行

    redis_searching = fetch_total_queue()

    #3.
    need_push = db_id_list.difference(redis_searching)
    if need_push:
        conn.lpush("DAY21_TASK_QUEUE",*need_push)


def update_order(order_id,status):
    db_update_order("update order_database set status = %s where id = %s",(status,order_id))


def get_order_object(order_id):
    res = fetch_one("select * from order_database where id = %s",[order_id])
    return res

def task():
    pass


def run():
    try:
        #初始化数据库未在队列中的订单
        db_queue_init()
        while True:
            #取队列中获取订单
            order_id = pop_queue()
            #print(order_id)
            if not order_id:
                continue


            #订单是否存在
            order_dict = get_order_object(order_id)
            if not order_dict:
                continue


            #更新订单状态
            update_order(order_id,2)

            #执行订单
            print("执行订单：",order_dict)


            #线程池
            thread_pool = ThreadPoolExecutor(30)
            for i in range(order_dict['count']):
                thread_pool.submit(task,order_dict)

            #关闭线程池
            thread_pool.shutdown()


            time.sleep(5)
            print("完成订单")


            # 更新订单状态
            update_order(order_id, 3)
    except KeyboardInterrupt:
        print("\n手动已停止程序...")
"""KeyboardInterrupt 是 Python 中的一个内置异常类，当用户在程序运行期间按下 Ctrl+C（或在某些系统上为 Delete）
组合键时触发。它属于系统退出异常，用于安全地中断长时间运行的任务或死循环，并允许程序在终止前执行清理工作（如关闭文件、数据库连接）。
"""

if __name__ == '__main__':
    run()