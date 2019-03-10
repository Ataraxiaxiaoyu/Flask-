# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os

app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/movie"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = '0add7b1ac0e94095b304bbbe5e908c16'
# 上传文件
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/media/")
# 存放用户头像
app.config['USER_IMAGE'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/user_image/')

db = SQLAlchemy(app)

app.config["REDIS_URL"] = "redis://64.154.38.54:6379/0 "


from flask_redis import FlaskRedis

rd = FlaskRedis(app)



#从前台，后台导入蓝图对象
from app.admin import admin as  admin_blueprint
from app.home import home as home_blueprint

# 使用app对象，调用register_blueprint函数进行蓝图的注册
# 第一个参数是蓝图，第二个参数是url地址的前缀。通过地址前缀划分前后台的路由
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(home_blueprint)


# 添加全局404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
