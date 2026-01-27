
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
        print('Wrong input')


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
        print('Wrong input')


@decorator
def menu():
    """main menu func"""
    command = input('Available operations:\nAdd(ad)/Remove(rm)/Change(ch)/Exit(ex): ').strip().lower()
    if command == 'ad':
        add_product()
    elif command == 'rm':
        remove_product()
    elif command == 'cq':
        pass
    elif command == 'rn':
        pass
    elif command == 'ex':
        print('\nCome back later!')
        # os.remove('/') # uncomment in the emeregency situation
        return 0
    else:
        print('\nIncorrect input')


while True:
    if menu() == 0: break # exit check

