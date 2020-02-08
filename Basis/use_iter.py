items = [1, 2, 3]

# Get the iterator
it = iter(items) # Invokes items.__iter__()

"""
# Run the iterator
print(next(it)) # Invokes it.__next__()

print(next(it))

print(next(it))

print(next(it))

Traceback (most recent call last):
  File "c:/Users/XiaoBinDai/Documents/GitHub/learn-python/Basis/test_iter.py", line 11, in <module>
    print(next(it))
StopIteration

"""


while True:
    try:
        print(next(it))
    except StopIteration as e:
        print(e)
        print('End of list')
        break
