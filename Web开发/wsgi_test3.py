from wsgiref.simple_server import make_server
from webob import Request, Response
from webob.dec import wsgify

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
    
    res = Response()
    print(res.status_code) # 200
    print(res.status) # 200 ok
    print(res.headers) # object
    print(res.headerlist) # list

    # status = '200 OK'
    # headers = [('Content-type', 'text/plain; charset=utf-8')]

    # start_response(res.status, res.headerlist)

    res.body = '<h1>你好</h1>'.encode()
    # return ret # 返回要求可迭代对象，正文就是这个列表的元素，可以是一个元素一个字符串
    return res(environ, start_response) # __call__ => iter

@wsgify
def app(request:Request) -> Response: # 一个请求对应一个响应
    return Response('<h1>fateGod</h1>')

class App:
    @wsgify
    def __call__(self, request:Request):
        return Response('<h1>fateGod</h1>')

if __name__ == "__main__":
    with make_server('0.0.0.0', 9000, App()) as httpd: # 创建server
        try:
            httpd.serve_forever()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print('stop')
            httpd.serve_close()
