
# main variable we will work with
product_list = {'bananas': 1,
                'beer cans': 10,
                'кириешки': 100500}


def decorator(func):
    """decorator that literally decorates"""
    def wrapper(*args, **kwargs):
        print('_' * 30)
        func(*args, **kwargs)
    return wrapper


def counter(func):
    """how many times did this function launched?"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'Func named "{func.__name__}" was launched {wrapper.count} times.')
        func(*args, **kwargs)
        return wrapper.count
    wrapper.count = 0
    return wrapper

