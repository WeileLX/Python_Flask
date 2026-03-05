#基于Flask快速开发某订单平台，实现频台下单后自动执行
"""
京东抢茅台：
        1.手机抓包 -> 登陆 -> cookie
        2.web界面， 提交 -> 数据库
        3. 获取cookie， 逐一抢

视频网站，刷播放量。
        1.web页面，下单；  URL， 500播放量
        2.运行 -> 30分钟
        3.web页面，状态更新（已完成）
-----------------------------------------------------------
用户表
|  id  |  mobile  |  password  |  real_name  |  role  |
------------------------------------------------------------
订单表
|  id  |  url  |  count  |  status  |  user_id  |
"""

from day20 import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)