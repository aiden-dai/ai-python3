"""
map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results.
"""

a = map(lambda x: x**2,range(5))
print(a)  # <map object at 0x0000014D2429DA20>

for i in a:
    print(i)


def say_hi(name):
    return 'Hello {}'.format(name)

    
say_hi('Tom')

b = map(say_hi, ['Tom', 'John', 'Kate'])
print(b)  # <map object at 0x000001ED9013D240>
for i in b:
    print(i)

c = list(map(say_hi, ['Tom', 'John', 'Kate']))
print(c)  # ['Hello Tom', 'Hello John', 'Hello Kate']