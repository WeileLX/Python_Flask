from flask import Blueprint, session, redirect, render_template, request
from utils import db
from utils import cache

od = Blueprint('od', __name__)


@od.route('/')
def index():
    return redirect('/login')

@od.route('/order/list')
def order_list():
    #读取cookie&解密获取用户信息
    user_info = session.get('user_id')
    role = user_info['role'] #1 客户， 2 管理员
    print(user_info)

    if role == '2':
#        result = db.fetch_all("select * from order_database",[])
        result = db.fetch_all("select * from order_database left join user_database on order_database.order_user_id = user_database.id;",[])
    else:
#        result = db.fetch_all("select * from order_database where order_user_id = %s", (user_info['id'],))
        result = db.fetch_all("select * from order_database left join user_database on order_database.order_user_id = user_database.id where order_user_id = %s", (user_info['id'],))

    status_return = {
        1:{"text":"待执行",'cls':"default"},
        2: {"text": "正在执行", 'cls': "primary"},
        3: {"text": "已完成", 'cls': "success"},
        4: {"text": "已失败", 'cls': "danger"}

    }
    print(result)
    return render_template("order_list.html",data_list=result,
                           status_return=status_return)


@od.route('/order/create',methods=['GET','POST'])

def order_create():
    #读取cookie&解密获取用户信息
    if request.method == 'GET':
        return render_template('order_create.html')

    url = request.form.get('url')
    count = request.form.get('count')
    user_info = session.get('user_id')

    params = (url,count,user_info['id'])
    order_id = db.insert("insert into order_database(url,count,order_user_id,status) value(%s,%s,%s,1)",params)

    cache.push_queue(order_id)

    return redirect('/order/list')

#f"Hello, {name}!"

@od.route('/order/delete')
def order_delete():
    #读取cookie&解密获取用户信息

    return "删除订单"