import redis, json


 #1 (output)print()********************************************************************************
"""
a=00
b=49
c=a+b
print(c)
print(a*b)

----------------------------------------------------------------------------------------
print(chr(98))    -  ascii 98 = 'b'
将字符转换为其Unicode码点 (整数)。
print(ord('a'))： = 97

----------------------------------------------------------------------------------------
写入文件：
fp = open('input.txt','w') -write
print("中文",file=fp)
fp.close()

----------------------------------------------------------------------------------------
end 结束符 & sep 自定义分隔符
print("rpi",end="-->")
print("exo")
== rpi-->exo

print("2025","01","15",sep="-")
==  2025-01-15

----------------------------------------------------------------------------------------
连接符
print("2025"+"2323")
print("2025"+2323)    :   Error, should use comma ',' ex: print("2025",2323) ==2025 2323
    print("2025",2323,sep='') == 20252323




#2 (input)input()********************************************************************************

name = input("enter name")
print(name)
----------all input will be a string-------


change to int or different variable type, use int(),or double
age = input("enter age")
age = int(age)
print(age+2)
input: 2, then + 2 ,output == 4


def is_valid_identifier(name):
    try:
        exec(f"{name} = None")    #将执行字符串形式的python代码
        return True
    except:
        return False
print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True
#eval() 将字符串当成表达式计算，返回结果。 for 循环以及赋值是不可以的.
eval("1 + 2 * 3")   # 7
eval("'hello'.upper()")  # 'HELLO'
eval("3 < 5")       # True

#可以用isidentifier()更加合规
print("2v".isidentifier())  # False


import sys
print('================Python import mode==========================')
print ('命令行参数为:')
#print(sys.argv)    -当前文件路径
#for i in sys.argv:
#    print (i)
#print ('\n python 路径为',sys.path)   -day20文件下的一张「Python 去哪里找东西的地址清单」


------------------------------------------------------------------------------------


print(help(print))        #输出字符串该函数定义
type()              #你是不是纯种哈士奇？
isinstance(x,int)        #你是不是狗？只要是这个类型或者它的子类都算：父类子类
bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
1 is True  >>> True
2 is False  >>> False
3 is True  >>> True


 Set - ExecutionPolicy - ExecutionPolicy
 RemoteSigned - Scope
 CurrentUser
 - 以管理员身份解开限制

 Set - ExecutionPolicy - ExecutionPolicy
 Undefined - Scope
 CurrentUser
 - 重新限制

 Get - ExecutionPolicy - List
 - 检查


a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)       #a去除b相同的元素
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

json.dumps(x) # 打包成JSON 对象
json.loads(x)# 解析JSON 对象

redis_conn = redis.Redis(host='localhost',
                          port=6379,
                          decode_responses=True)

tasks = redis_conn.rpop("spider_task_list")    #右边pop
json_tasks =json.loads(tasks)
print(json_tasks, type(json_tasks))



import random

random.seed(11)
print(random.random())
print(random.random())

random.seed(11)
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

import time

# for i in range(101): # 添加进度条图形和百分比
#     bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='', flush=True)
#     time.sleep(0.05)

# print()

str="run.runoob.com                  run"
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))

str = "runoob菜鸟教程"
print (str.isalpha())


dict_ = {"1":1,"2":2,"3":3,"4":4}

dict_key = dict_.keys()
dict_value = dict_.values()

n = 0

for i in dict_value:
    n = n + i

print(n)

l = list(dict_value)
print(l)
del dict_['1']

print(dict_value)
dict_['5'] = 5
print(dict_value)





with open('test.txt', 'r') as file:

    content = file.read()


    print(content)
# 文件已自动关闭



def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        max = i
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                max = j
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = base




    插入排序
    # 外循环：已排序区间为 [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # 内循环：将 base 插入到已排序区间 [0, i-1] 中的正确位置
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]  # 将 nums[j] 向右移动一位
            j -= 1
        nums[j + 1] = base  # 将 base 赋值到正确位置


if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("插入排序完成后 nums =", nums)


redis_conn_params = redis.Redis(host='localhost',
                                    port=6379,
                                    decode_responses=True)
data = redis_conn_params.hget('spider_result_list', '8ec03f0e-8993-498c-8475-5cd139f5d914')

print(data)
redis_conn_params.hdel('spider_result_list', '8ec03f0e-8993-498c-8475-5cd139f5d914')
"""



