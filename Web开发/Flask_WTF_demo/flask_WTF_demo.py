#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 13:41
# @Author  : YuHao
# @File    : flask_WTF_demo.py

# 1. 导入Flask扩展
from flask import Flask, render_template, request

app = Flask(__name__)

'''
目的：实现一个简单的登录的逻辑处理
1. 路由需要有get和post两种请求方式 --> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题，就返回一个success
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    # request: 请求对象 --> 获取请求方式，数据

    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            print('参数不完整')
        elif password != password2:
            print('密码不一致')
        else:
            return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
