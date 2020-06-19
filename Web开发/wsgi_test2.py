from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

# A 127.0.0.1:9000?id=1&name=tome&age=20
# 127.0.0.1:9000?id=1&name=tome,jerry&age=20&age=30
def simple_app(environ:dict, start_response):
    # 查询字符串
    query_string = environ.get('QUERY_STRING')
    print(query_string)
    # d = {}
    # for item in query_string.split('&'):
    #     k,_,v = item.partition('=')
    #     d[k] = v
    
    # d = {k:v for k,_,v in map(lambda x: x.partition('='), query_string.split('&'))}

    qs = parse_qs(query_string)
    print(qs)
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [query_string.encode()]
    return ret # 返回要求可迭代对象，正文就是这个列表的元素，可以是一个元素一个字符串

with make_server('0.0.0.0', 9000, simple_app) as httpd: # 创建server
    try:
        httpd.serve_forever()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('stop')
        httpd.serve_close()
