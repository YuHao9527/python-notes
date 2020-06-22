# Flask简介：

Flask诞生于2010年，是用python语言基于werkzeug工具箱编写的轻量级Web开发框架。

Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展(邮件扩展Flask-Mail，用户认证Flas-Login) ，都需要用第三方的扩展来实现。

其WSGI工具箱采用Werkzeug（路由模块），模板引擎则使用Jinja2。这两个也是Flask框架的核心。

Python最出名的框架要数Django。此外还有Flask、Tornado等框架。虽然Flask不是最出名的框架，但是Flask应该算是最灵活的框架之一，这也是Flask受到广大开发者喜爱的的原因。

Flask常用扩展包：

- Flask-SQLalchemy: 操作数据库；
- Flask-migrate: 管理迁移数据库；
- Flask-Mail: 邮件；
- Flask-WTF: 表单；
- Flask-Bable: 提供国际化和本地化支時，翻译；
- Flask-script: 插入脚本；
- Flask-Login: 认证用户状态；
- Flask-OpenID: 认证；
- Flask-RESTful: 开发REST API的工具，
- Flask-Bootstrap: 集成前端Twitter Bootstrap框架；
- Flask-Moment: 本地化日期和时间；
- Flask-Admin: 简单而可扩展的管理接口的框架

`扩展列表： http://flask.pocoo.org/extensions/`

1. 中文文档(https://dormousehole.readthedocs.io/en/latest/)
2. 英文文档(https://flask.palletsprojects.com/en/1.1.x/)

## Django与Flask之间的差别

- Django功能大而全，Flask只包含基本的配置
Django一站式解决的思路，能让开发者不用在开发之前就在选择应用的基础设施上花费大时间。
Django有模板，表单，路由，认证，基本的数据库管理等等内建功能。与之相反，Flask只是一个内核，默认依赖于两个外部库： Jinja2模板引擎和Werkzeug WSGI工具集，其他很多功能都是以扩展的形式进行嵌入使用。
- Flask 比 Django 更灵活
- Flask 在 Django 之后发布，现阶段有大量的插件和扩屐满足不同需要
- Django发布于2005年，Flask创始于2010年年中。

## 从Hello World开始

### Flask程序运行过程

1. 当客户端想要取资源时，一般会通过浏览器发起HTTP请求。
2. 此时，Web服务器会把来自客户端的所有请求都交拾Flask程序实例
3. 程序实例使用Werkzeug来做路由分发(URL请求和视图函数之间的对应关系）。
4. 根倨每个URL请求，找到具体的视图函并进行调用。
   - 在Flask程序中，路由的实现一般是通过程序实例的装饰器实现。
5. Flask调用视图函数后，可以返回两种内容:
   - 字符串内容: 将视图函数的返回值作为响应的内容，返回给客户端(浏览器从)
   - HTML模板内容: 获取数据后，把数据传入HTML模板文件中，模板引擎负责渲染HTTP响应数据，然后返回响应数据给客户端(浏览器)

### 示例:

- 新建Flask项目
- 导入Flask类

`from flask import Flask`

- Flask函数接收一个**参数name**，它会指向程序所在的模块

`app = Flask(__name__)`

- 装饰器的作用是将路由映射到视图函数index
```python
@app.route('/')
def index():
    return 'Hello, Flask'
```
