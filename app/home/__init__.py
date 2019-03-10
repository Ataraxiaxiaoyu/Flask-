# coding:utf-8

from flask import Blueprint

#传入两个参数，一个是蓝图名称，一个是name值
home = Blueprint("home", __name__)

import app.home.views