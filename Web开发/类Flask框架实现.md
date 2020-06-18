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
