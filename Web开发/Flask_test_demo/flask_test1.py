#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 13:41
# @Author  : YuHao
# @File    : flask_test1.py

# 1. 导入Flask扩展
from flask import Flask, render_template

# 2. 创建Flask应用程序实例
# 需要传入__name__，作用是为了确定资源所在的路径
app = Flask(__name__)

# 3. 定义路由及视图函数
# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index():
    return 'Hello, Flask'
    # return render_template('index.html')

# 4. 启动程序
if __name__ == '__main__':
    # 执行了app.run()。就会将Flask程序运行在一个简易的服务器(Flask提供的，用于测试的)
    app.run()
