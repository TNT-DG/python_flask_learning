# -*- coding: utf-8 -*-

import os

# 开关调试模式
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

# session必须要设置key
SECRET_KEY = os.urandom(24)

# mysql数据库连接信息
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sf123@localhost:3306/zlkt_demo?charset=utf8"
