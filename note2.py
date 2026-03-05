"""def insert(x):
    x.append([1,2,3,4,5,6])
    x[1] = 1122
    x[4][2] = 0
    return



x = [1,2,3,4]
insert(x)

print(x)"""



def logger(func):
    def wrapper(*args,**kwargs):
        print('start')
        func(*args,**kwargs)
        print('finish')
    return wrapper

@logger
def print_hello(x):
    print(f"hello {x}")

if __name__ == "__main__":
    print_hello('zhangsan')


一、__init__ 是什么？
1️⃣ 先一句话版本

__init__ = 对象出生时自动执行的函数

2️⃣ 生活比喻

你去买一台新电脑：

出厂时：

装系统

设置语言

分配硬盘

👉 这些“出生时要做的事”，就是 __init__

3️⃣ 最简单的例子
class Person:
    def __init__(self):
        print("一个人被创建了")

p = Person()

输出：

一个人被创建了

说明：

👉 你一写 Person()，__init__ 就会自动运行

4️⃣ self 是谁？
def __init__(self):

self = 正在被创建的那个对象本身

你不用手动传，Python 自动帮你传。

二、*args 是什么？
1️⃣ 一句话版本

*args = 把“很多位置参数”打包成一个盒子（元组）

2️⃣ 不用类，先看函数
def f(*args):
    print(args)

f(1, 2, 3)

输出：

(1, 2, 3)

👉 所有多余的参数，被装进了一个“盒子”

3️⃣ 为什么要它？

如果不用 *args：

def f(a, b, c):
    ...

参数个数固定，很死。

用了 *args：

def f(*args):
    ...

👉 想给几个就给几个

4️⃣ 在你那段代码里的作用
def __init__(self, *args, **kwargs):
    self.wrapped = cls(*args, **kwargs)

意思是：

👉 Wrapper 不管原来的类要几个参数，都原封不动转交

现在你只要记住：

*args = “我全收，不挑”

三、**kwargs 是什么？
1️⃣ 一句话版本

**kwargs = 把“带名字的参数”装进一个字典

2️⃣ 例子
def f(**kwargs):
    print(kwargs)

f(name="张三", age=18)

输出：

{'name': '张三', 'age': 18}
3️⃣ *args vs **kwargs
写法	收什么
*args	没名字的
**kwargs	有名字的
4️⃣ 现在你只需要这样记：

*args, **kwargs = “不管你传什么参数，我都接住”

四、__getattr__ 是什么？（最难但最关键）
1️⃣ 一句话人话版

当你访问一个不存在的属性时，Python 会自动来问 __getattr__

2️⃣ 例子（不用装饰器）
class A:
    def __getattr__(self, name):
        print(f"你在找 {name}，但我没有")

a = A()
a.abc

输出：

你在找 abc，但我没有

👉 Python 发现 abc 不存在，就调用了 __getattr__

3️⃣ 再来一个“转发”的例子
class B:
    def say(self):
        print("hello")

class A:
    def __init__(self):
        self.b = B()

    def __getattr__(self, name):
        return getattr(self.b, name)

a = A()
a.say()

输出：

hello

意思是：

A 没有 say
👉 就去 B 那里找

4️⃣ 回到你原来的代码
def __getattr__(self, name):
    return getattr(self.wrapped, name)

翻成人话：

Wrapper 自己没有的属性
👉 全部交给真正的 MyClass

所以你才能：

obj.display()

感觉自己在用 MyClass，其实是在用 Wrapper

五、把 4 个东西连成一句话（终极理解）

当你创建对象时
👉 __init__ 自动执行
👉 *args, **kwargs 保证参数不丢
👉 真正的对象被藏在 wrapped 里
👉 如果 Wrapper 没这个功能
👉 __getattr__ 自动转发给原对象

六、你现在的水平判断（很重要）

如果你现在能理解：

✔ __init__ 是自动调用
✔ *args, **kwargs 是“全接收”
✔ __getattr__ 是“兜底转发”

👉 你已经看懂了 Python 类的核心机制

装饰器只是外壳。