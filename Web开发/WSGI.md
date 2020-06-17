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
