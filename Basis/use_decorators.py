def say_hi(name):
    print('Hello, {}'.format(name))


def wrap(func):

    def wrap_func(name):
        print('Pre-func')
        func(name)
        print('After-func')
    
    return wrap_func

say_hi = wrap(say_hi)
say_hi('Tom')

print('-'*20)

import functools

def wrap2(func):
    @functools.wraps(func)
    def wrap_func(name):
        print('Pre-func')
        func(name)
        print('After-func')
    return wrap_func


@wrap2
def say_hi2(name):
    print('Hello, {}'.format(name))

say_hi2('Tom')

