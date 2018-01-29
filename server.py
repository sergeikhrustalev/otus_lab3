from urllib.parse import parse_qs
from route_map import VIEW_ROUTE_MAP


def get_kwargs_from_query_string(query_string):
    return parse_qs(query_string)


def application(environ, start_response):

    response_status = '404 NOT FOUND'
    response_content = 'Not Found'

    for request_method, path_info, mapped_function in VIEW_ROUTE_MAP:

        if (
                request_method == environ.get('REQUEST_METHOD') and
                path_info == environ.get('PATH_INFO')
        ):
            response_status = '200 OK'

            if request_method == 'GET':
                response_content = mapped_function(
                    **get_kwargs_from_query_string(environ.get('QUERY_STRING'))
                )
            else:
                response_content = mapped_function()

            break

    start_response(response_status, [('Content-Type', 'text/plain')])
    return [response_content.encode()]
