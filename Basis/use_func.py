
# arg -> Tuple
def hello(greeting, *args):
    if (len(args) == 0):
        print('{}! '.format(greeting))
    else:
        print('{}, {}!'.format(greeting, ', '.join(args)))


hello('Hello')
hello('Hello', 'Tom', 'John')

names = ('Tom', 'John')
hello('Hello', *names)

# kwarg -> dist
def hello2(**kwarg):
    for arg, value in kwarg.items():
        print('{} = {}'.format(arg, value))


data = {'a':1, 'b':2, 'c':3}
hello2(a=1, b=2, c=3)
hello2(**data)

