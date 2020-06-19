# 类Flask框架实现

从现在开始，我们将一步步完成一个WSGI的WEB框架，从而了解WEB框架的内部机制。

## WSGI请求environ处理

WSGI服务器程序会帮我们处理HTTP请求报文，但是提供的environ还是一个用起来不方便的字典

```shell
http://127.0.0.1:9999/python/index.html?id=1234&name=tom
('SERVER_PROTOCOL','HTTP/1.1')
('wsgi.url scheme', 'http')
('HTTP_HOST', '127.0.0.1:9999')
('SERVER_PORT', '9999')
('REMOTE_ADDR ', '127.0.0.1')

('REQUEST_METHOD', 'GET')
('CONTENT_TYPE', 'text/plain')
('PATH_INFO', '/python/index.html')
('QUERY_STRING ', 'id=1234&name=tom')
('HTTP_USER_AGENT', 'Mozilla/5.0 (Windows NT 6.1) App1eWebKit/537.36(KHTML, like Gecko) Maxthon/5.0 Chrome/55.0.2883.75 Safari/537.36')
)
```

## QUERY_STRING 查询字符串的解析

WSGI服务器程序处理过HTTP报文后，返回一个字典，可以得到查询字符串`('QUERY_STRING', 'id=1234&name=tom')`。这个键值对用起来不方便。

1. 编程解析

    ```python
    qstr = environ.get('QUERY_STRING')
    print(qstr)
    if qstr:
        for pair in qstr.split('&'):
            k, _, v = pair.partition('=')
            print("k={}, v={}".format(k, v))
    ```

    ```python
    # id=5&name=tom
    qstr = environ.get('QUERY_STRING')
    if qstr:
        querydict = d = {k:v for k,_,v in map(lambda x: x.partition('='), query_string.split('&'))}
    print(querydict)
    ```

2. 使用cgi模块

    ```py
    # id=5&name=tom
    qstr = environ.get('QUERY_STRING')
    print(qstr)
    print(parse_qs(qstr))
    # {'name': ['tom'], 'id': [‘5’]}
    ```

可以看到使用这个库，可以解析查询字符串，请注意value是列表，为什么？
这是因为同一个key可以有多个值。
cgi模块过期了，建议使用urlib

3. 使用urlib库

    ```py
    # http://127.0.0.1:9999/?id=5&name=wayne&age=&comment=1,a,c&age=19&age=20
    qstr = environ.get('QUERY STRING')
    print(qstr)
    print(parse.parse_qs(qstr)) # 字典
    print(parse。parse_qsl(qstr)# 二元组列表

    # 运行结果
    id=5&name=wayne&age=&comment=1,a,c&age=19&age=20
    {'id': ['5'], 'name': ['wayne'], 'comment': ['1,a,c'], 'age': ['19', '20']}
    [('id', '5'), ('name', 'wayne'), ('comment', '1,a,c'), ('age', '19'), ('age', '20')]
    ```

parse_qs函数，将一个名称的多值，保存在字典中，使用了列表保存。
comment=1,a,c这不是多值，这是一个值。
age 是多值。

## environ的解析——webob库

环境数据狠多，都是存在字典中的，字典的存取方式没有对象的属性访问方便。
使用第三方库webob，可以把环境数据的解析、封装成对象。

### webob简介

python下，可以对WSGI请求进行解析，并提供对响应进行高级封装的库。

`$ pip install webob`

官方文档[docs.webob.org](docs.webob.org)

### webob.Request对象

将环境参数解析并封装成request对象
GET方法，发送的数据是URL中Query_string，在Request Header中。
request.GET就是一个字典MultiDict，里面就封装着查询字符串。
