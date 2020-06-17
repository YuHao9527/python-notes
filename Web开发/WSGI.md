# WSGI

![WSGI](images/wsgi.jpg "WSGI")

WSGI 主要规定了服务器端和应用程序间的接口。

## WSGI 服务器——wsgiref

wsgiref这是一个WSGI参考实现库
wsgiref.simple_server 模块实现一个简单的WSGI HTTP服务器。

`wsgiref.simple_server.make_server(host, port, app,server_c1ass=WSGIServer,handler c1ass=WSGIRequestHand1er)`启动一个WSGI服务器
`wsgiref.simple_server.demo_app(environ, start_response)`一个函数，小巧完整的WSGI的应用程序的实现

```python
# 返回文本例子
from wsgiref.simple_server import make_server, demo_app
ip = '127.0.0.1'
port = 9999
server = make_server(ip, port, demo_app) # demo_app应用程序，可调用
server.serve_forever() # server.handle_request() 执行一次
```

WSGI 服务器作用

- 监听HTTP服务端口(TCPServer, 默认端口80)
- 接收浏览器端的HTTP请求并解析封装成environ环境数据
- 负责调用应用程序，将environ和start_response方法传入
- 将应用程序响应的正文封装成HTTP响应报文返回浏览器端

## WSGI APP应用程序端

1. 应用程序应该是一个可调用对象

    Python中应该是函数、类、实现了`__call__`方法的类的实例

2. 这个可调用对象应该接收两个参数

    ```python
    # 1 函数实现
    def application(environ, start_response):
        pass

    # 2 类实现
    class Application:
        def __init__(self, environ, start_response):
            pass

    # 3 类实现
    class Application:
        def __call__(self, environ, start_response):
            pass

    ```

3. 以上的可调用对象实现，都必须返回一个可迭代对象

    ```python
    res_str = b'baidu.com\n'

    # 函数实现
    def application(enviro, start_respose):
        return [res_str]

    # 类实现
    class Application:
        def __init__(self, environ, statrt_response):
            pass
        def __iter__(self): # 实现此方法，对象即可迭代
            yield res_str

    # 类实现
    class Application:
        def __call__(self, environ, start_response):
            return [res_str]

    ```

environ和start_response这两个参数名可以是任何合法名，但是一般默认都是这两个名字。

### environ

environ是包含Http请求信息的dict对象

|名称|含义|
|---|---|
|REQUEST_METHOD|请求方法，GET、POST等|
|PATH_INFO|URL中的路径部分|
|QUERY_STRING|查询字符串|
|SERVER_NAME, SERVER_PORT|服务器名、端口|
|HTTP_HOST|地址和端口|
|SERVER_PROTOCOL|协议|
|HTTP_USER_AGENT|UserAgent信息|
