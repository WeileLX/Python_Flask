from flask import Blueprint


od = Blueprint('od', __name__)

@od.route('/order/list')
def order_list():
    return "订单列表"

@od.route('/order/create')
def order_create():
    return "创建订单"