from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ:dict, start_response):
    
    for k, v in environ.items():
        print(k, v)
    print('-'*30)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret # 返回要求可迭代对象，正文就是这个列表的元素，可以是一个元素一个字符串

with make_server('0.0.0.0', 9000, simple_app) as httpd: # 创建server
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.serve_close()
