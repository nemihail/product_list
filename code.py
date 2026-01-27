
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


@decorator
@counter
def add_product():
    try:
        name = input('Product name to add: ')
        if name in product_list.keys():
            command = input(f'\nProduct named "{name}" already exists.\nDo you want to update its quantity ({product_list[name]})? [y/n]: ')
            if command == 'y':
                pass
            elif command == 'n':
                return 0
            else:
                print('Input is incorrect')
        product_list.update({
            name:
            int(input('Product quantity: '))
        })
    except TypeError:
        print('Suka ti tupoi blyat')


@decorator
@counter
def remove_product():
    name = input('Product name to remove: ')
    if name in product_list.keys():
        del product_list[name]
    else:
        print('There is nothing to remove')


@decorator
@counter
def replace_product():
    try:
        name = input('Product name to replace: ')
        if name in product_list.keys():
            del product_list[name]
        else:
            print('There is nothing to replace')
        product_list.update({
            name:
            int(input('Product quantity: '))
        })
    except TypeError:
        print('Suka ti tupoi blyat')

