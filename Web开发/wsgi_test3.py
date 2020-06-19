from wsgiref.simple_server import make_server
from webob import Request, Response

# A 127.0.0.1:9000?id=1&name=tome&age=20
# 127.0.0.1:9000?id=1&name=tome,jerry&age=20&age=30
def simple_app(environ:dict, start_response):
    request = Request(environ)

    method = request.method

    print(method)
    print(request.GET) # dict
    print(type(request.GET))
    print(request.POST) # dict
    # http://127.0.0.1:9000/user/?id=1000&name=jerry
    print(request.path) # 路径
    print(request.params) # 所有参数
    print(request.headers) # 请求头
    
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = []
    return ret # 返回要求可迭代对象，正文就是这个列表的元素，可以是一个元素一个字符串

with make_server('0.0.0.0', 9000, simple_app) as httpd: # 创建server
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.serve_close()
