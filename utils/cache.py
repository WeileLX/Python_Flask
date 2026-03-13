import redis

POOL = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True,max_connections=1000)

def push_queue(value):
    conn = redis.Redis(connection_pool=POOL)
    conn.lpush("DAY21_TASK_QUEUE",value)

