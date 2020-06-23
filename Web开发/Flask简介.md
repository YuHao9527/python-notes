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

## 路由定义的基本方式

### 请求方式限定

使用methods参数指定可接受的请求方式，可以是多种
```python
@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'hello world'
```

### 给路由传参示例

有时我们需要将同一类URL映射到同一个视图函数处理，比如：使用一个视图函数来显示不同用户的订单信息。

路由传递的参数默认当作string处理

```python
@app.route('/orders/<order_id>')
def hello_itheima(order_id):
    # 此处的逻辑：去查询数据库改用户的订单信息，比返回
    print(type(order_id)) # 类型为unicode
    return 'hello itcast %d' % order_id
```

这里会指定int，会调用系统的路由转换器进行匹配和转换

```
- 大致原理是将参数强转为int，如果成功，则可以进行路由匹配
- 如果参数无法转换成功，就无法匹配路由
```

```python
@app.route('/orders/<int: order_id>')
def hello_itheima(order_id):
    print(type(order_id)) # 类型为int
    return 'hello itcast %d' % order_id
```

## Jinja2模板引擎

### 模板

在前面的示例中，视图函数的主要作用是生成请求的响应，这是最简单的请求。实际上，视
图函数有两个作用：处理业务逻辑和返回响应内容。在大型应用中，把业务逻辑和表现内容
放在一起，会增加代码的复杂度和维护成本。本节学到的模板，它的作用即是承担视图函数
的另一个作用，即返回响应内容。

- 模板其实是一个包含响应文本的文件，其中用占位符（变量）表示动态部分，告诉模板引擎
其具体的值需要从使用的数据中获取
- 使用真实值替换变量，再返回最终得到的字符串，这个过程称为“渲染”
- Flask是使用Jinja2这个模板引擎来渲染模板

使用模板的好处
- 视图函数只负责业务逻辑和数据处理（业务逻辑方面）
- 而模板则取到视图函数的数据结果进行展示（视图展示方面）
- 代码结构清晰，耦合度低

## Jinja2
### 两个概念：
- Jinja2: 是Python下一个被广泛应用的模板引擎，是由Python实现的模板语言，他的
设计思想来源于Django的模板引擎，并扩展了其语法和一系列强大的功能，其是Flask内
置的模板语言。
- 模板语言: 是一种被设计来目动生成文档的简单文本格式，在模板语言中，一般都会把
一些变量传结模板，替换模板的特定位置上预先定义好的占位变量名。

### 渲染模板函数

- Flask提供的`render_template`函数封装了该模板引擎
- `render_template`函数的第一个参数是模板的文件名，后面的参数都是键值对，表
示模板中变量对应的真实值

### 使用

#### 注释

- 使用{# #}进行注释
`{# {{ name }} #}`

#### 变量代码块

- {{}}来表示变量名，这种{{}}语法叫做**变量代码块**
`{{ post.title }}`

Jinja2模板中的变量代码块可以是任意Python类型或者对象，只要它能够被Python的
str()方法转换为一个字符串就可以，比如，可以通过下面的方式显示一个字典或者列表
中的某个元素：
```jinja2
{{your_dict['key']}}
{{your_list[0]}}
```

#### 控制代码块

- 用{%%}定义的**控制代码块**，可以实现一些语言层次的功能，比如循环或者if语句

```jinja2
{% if user %}
    {{ user }}
{% else %}
    hello!

{% for index in indexs %}
    {{ index }}
{% endfor %}
```

### 过滤器

过滤器的本就质是函数。有时候我们不仅仅只是需要输出变量的值，我们还需要修改变
变量的显示，甚至格式化、运算算等等，而在模板中是不能直接调用Python中的某些方
法，那么这就用到了过滤器。

使用方式：
- 过滤器的使用方式为：变量名|过滤器。
```jinja2
{{variable | filter_name(*args)}}
```
- 如果没有任何参数传给过滤器，则可以把括号省酪掉
```jinja2
{{variable | filter_name}}
```
- 如："，这个过滤器的作用：把变量variable的值的首字母转换为大写，其他字母
转换为小写

#### 链式调用
在jinja2中，过滤器是可以支持链式调用的，示例如下：
```jinja2
{{ "hello world" | reverse | upper }}
```
#### 常见内建过滤器

##### 字符串操作

- safe: 禁用转义
```jinja
<p>{{ '<em>hello</em>' | safe }}</p>
```

- capitalize: 把变量值的首母转字成大写，其余字母转小写
```jinja2
<p>{{ 'hello' | capitalize }}</p>
```
- lower：把值转成小写
```jinja2
<p>{{ 'HELLO' | lower }}</p>
```
- upper: 把值转成大写
```jinja2
<p>{{ 'hello' | upper }}</p>
```
- title: 把值中的每个单词的首字母都转成大写
```jinja2
<p>{{'hello' | title }}</p>
```
- reverse: 字符串反转
```jinja2
<p>{{ 'olleh' | reverse }}</p>
```
- format: 格式化输出
```jinja2
<p>{{ '%s is %d' | format('name', 17) }}</p>
```
- striptags：渲染之前把值中所有的HTML标签都删掉
```jinja2
<p>{{ '<em>hello</em>' | striptags }}</p>
```
- truncate: 字符串截断
```jinja2
<p>{{ 'hello every one' | truncate(9) }}</p>
```

##### 列表操作

- first：取第一个元素
```jinja2
<p>{{ [1,2,3,4,5,6] | first }}</p>
```
- last: 去最后一个元素
```jinja2
<p>{{ [1,2,3,4,5,6] | last }}</p>
```
- length: 获取列表长度
```jinja2
<p>{{ [1,2,3,4,5,6] | length }}</p>
```
- sum: 列表求和
```jinja2
<p>{{ [1,2,3,4,5,6] | sum }}</p>
```
- sort: 列表排序
```jinja2
<p>{{ [6,3,5,2,1,4] | sort }}</p>
```

##### 语句块过滤
```jinja2
{% filter upper %}
    一大堆字
{% endfilter %}
```

## Web表单

web表单是web应用程序的基本功能。

它是HTML页面中负责数据采集的部件。表单有三个部分组成：表单标签、表单域、表
单按钮。表单允许用户输入数据，负责HTML页面数据采集，通过表单将用户输入的数
据提交给服务器。

在Flask中，为了处理web表单，我们一般使用Flask-WTF扩展，它封裝了WTForms,
并且它有验证表单数据的功能.
### WTForms支持的HTML标准字段
字段对象|说明
-------|--
StringField|文本字段
TextAreaField|多行文本字段
PasswordField|密码文本字段
HiddenField|隐藏文件字段
DateField|文本字段，值为datetime.date文本格式
DateTimeField|文本字段，值为datetime.datetime文本格式
IntegerField|文本字段，值为整数
DecimalField|文本字段，值为decimal.Decimal
FloatField|文本字段，值为浮点数
BooleanField|复选框，值为True和False
RadioField|一组单选框
SelectField|下拉列表
SelectMutipleField|下拉列表，可选择多个值
FileField|文件上传字段
SubmitFieId|表单提交按钮
FormField|把表单作为字段嵌入另一个表单
FieldList|一组指定类型的字段

### WTForms常用验证函数

验证函数|说明
-------|--
DataRequired|确保字段中有数据
EqualTO|比较两个字段的值，常用于比较两次密码输入
Length|验证输入的字符串长度
NumberRange|验证输入的值在数字范围内
URL|验证URL
AnyOf|验证输入值在可选列表中
NoneOf|验证输入值不在可选列表中
使用配Flask-WTF需要配置参数SECRECT_KEY。
CSRF_ENABLED是为了CSRF（跨站请求伪造）保护。SECRET_KEY用来生成加密令牌，
当CSRF激活的时候，该设置会根据设置的密匙生成加密令牌。在HTML页面中直接写
form表单。

### 示例：

#### 使用普通方法实现表单

##### 在HTML页面中直接写form表单：

```jinja2
<form method="post">
    <lael>用户名:</lael><input type="text" name="username"><br>
    <label>密码:</label><input type="text" name="password"><br>
    <label>确认密码:</label><input type="text" name="password2"><br>
    {% for message in get_flashed_message() %}
        {{ message }}
    {% endfor %}
</form>
```

##### 视图函数中获取表单数据：

```python
from flask import Flask, render_template, request

app.secret_key = nihao

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # 1. 判断请求方式是post
    if request.method == 'POST':
        # 2. 获取参数，并校验参数完整性，如果有问题就进行flash
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username, password, password2]):
            flash('params error') 
        
        # 3. 校验密码
        elif password != password2:
            flash('password error')
        
        # 4. 没有问题就返回'success'
        else:
            print username
            return 'success'
    return render_template('wtf.html')
```

##### 使用Flask-WTF实现表单

