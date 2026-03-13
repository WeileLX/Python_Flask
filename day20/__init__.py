#FLASK 小蓝图
import redis,flask_session
from flask_session import Session
from flask import Flask, request, session, redirect



"""
普通flask session (默认cookie存数据)
    -游览器发送请求：”服务器我想登录，你给我一个session（会话）“
    -用户登录（POST请求），成功后创建session数据
    -session是一个字典
        可以：
            session["user_id"] = 2
            session["name"] = "tom"
        或者直接序列化：
            session["user_id"] = {"role":role,"real_name":result['real_name'],"id":result['id']}
        
    -用secret_key生成签名,签名保证cookie内容不会被篡改。比如最终cookie是： 389j29yu8r92yr389jwwdoadio1.abc123
    -Flask返回HTTP响应，同时在响应头里加上cookie.
    -游览器保存cookie
    -用户发送新的请求：
        -FLASK 拿到cookie，验证签名是否和secret_key匹配，如果匹配就安全
        然后解码。得到最终数据然后成功。

REDIS SESSION
    -post
    -flask_session生成session_id 比如：mvw83940thfg780w34yt78ghw-0438-t-923y3hw
        redis存一条记录：
                        key: session:tJ5Zl2dopuQP_YwgY1-WKEJEB00ORNy4i_JNbVkN1s8
                        value: {"_permanent":false,"user_id":2,"name":"tom"}
                        类型: string（序列化后的字典）
    -游览器存储session_id:
            set-cookie: mvw83940thfg780w34yt78ghw-0438-t-923y3hw 
    -当用户访问新页面。GET /profile
        Flask 拿session_id去redis查。
    得到数据就去渲染页面。记住是去调用该id的页面而不是查看该用户是否正确 。


"""

def auth():
    if request.path.startswith('/static'):
        return

    if request.path == '/login':
        return
    user_info = session.get("user_id")      #读取cookie&解密获取用户信息
    if not user_info:
        return redirect('/login')


def get_real_name():
    user_info = session.get('user_id')
    real_name = user_info['real_name']
    return real_name


def create_app():
    app = Flask(__name__)

    """
    # 必须有
    app.secret_key = "abc123"

    # session 存储方式
    app.config["SESSION_TYPE"] = "redis"

    # Redis地址
    app.config["SESSION_REDIS"] = redis.Redis(host="127.0.0.1", port=6379)

    # 初始化
    Session(app)
"""

    #cookie 存储 session
    app = Flask(__name__)
    app.secret_key = "abc123"  
    


    from .views import account
    from .views import order
    app.register_blueprint(order.od)
    app.register_blueprint(account.ac)

    app.before_request(auth)
    app.template_global()(get_real_name)
    return app