import hashlib
import redis,json


# 1.redis获取任务
def get_task():
    redis_conn_params = redis.Redis(host='localhost',
                                    port=6379,
                                    decode_responses=True)
    data = redis_conn_params.rpop('spider_task_list')
    data = json.loads(data)

    #    print(data)
    for i in data.values():
        print(i)
    return data




def set_result(tid, value):
    redis_conn_params = redis.Redis(host='localhost',
                                    port=6379,
                                    decode_responses=True)
    redis_conn_params.hset('spider_result_list',tid,value)




def run():

    task = get_task()
    ordered_string = task['data']
    encrypt_string = ordered_string + "8923u8dh29u92d32"
    obj = hashlib.md5(encrypt_string.encode())
    sign = obj.hexdigest()

    #---------------------------------------------------------------

    set_result(task['tid'],sign)







    #pass

if __name__ == '__main__':
    run()