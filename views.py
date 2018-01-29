from datetime import datetime
import random


def greetings(**query_params):
    name = query_params.get('name', ['Anonymous'])[0]
    return 'Hello, {} !!!'.format(name)


def show_datetime():
    current_datetime = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    return 'Current datetime: {}'.format(current_datetime)


def choice_random_int_number(**query_params):
    min = int(query_params.get('min', '0')[0])
    max = int(query_params.get('max', '0')[0])

    if min > max:
        return 'Min value must be less then max'

    return str(random.randint(min, max))
