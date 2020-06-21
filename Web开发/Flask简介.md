# FIask简介：

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

1. 中文文档(http://docs.jinkan.org/docs/flask/)
2. 英文文档(http://flask.pocoo.org/docs/0.12/)
