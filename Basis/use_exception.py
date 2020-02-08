# Define Error
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n




def bar():
    try:
        foo('0')
    except FooError as e:
        print('FooError!')
        print(e)




bar()
# foo('0') Raise Error