from views import *

VIEW_ROUTE_MAP = [
    ('GET', '/hello', greetings),
    ('GET', '/datetime', show_datetime),
    ('GET', '/choice', choice_random_int_number)
]
