#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 13:41
# @Author  : YuHao
# @File    : flask_test2.py

from flask import Flask, render_template

app = Flask(__name__)

# 1. 如何返回一个网页
# 2. 如何给模板填充数据
@app.route('/')
def index():
    # 比如需要传入网址
    url_str = 'www.baidu.com'

    my_list = [1, 3, 5, 7, 9]

    my_dict = {
        'name': 'Tom',
        'url': 'www.baidu.com'
    }

    # 通常， 模板中使用的变量名和要传递的数据的变量名保持一致
    return render_template('index.html', url_str=url_str, my_list=my_list, my_dict=my_dict)

if __name__ == '__main__':
    app.run()
