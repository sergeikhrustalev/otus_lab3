

def hello_man():
    return 'Hello man'

def your_age():
    return '22 age'

def test():
    return '555'


ROUTE_MAP = [
    ('GET', '/hello', hello_man),
    ('GET', '/age', your_age),
    ('GET', '/hello/6', test),
]



def application(environ, start_response):

    response_status = '404 NOT FOUND'
    response_content = 'Not Found'

    for request_method, path_info, view_function in ROUTE_MAP:
        if request_method == environ.get('REQUEST_METHOD') and path_info == environ.get('PATH_INFO'):
            response_status = '200 OK'
            response_content = view_function()
            break
    
    
    start_response(response_status, [('Content-Type', 'text/plain')])
    return [response_content.encode()]
