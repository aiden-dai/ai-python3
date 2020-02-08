# There are three basic sequence types: lists, tuples, and range objects.


"""
tuple: Tuples are immutable sequences
Example, x = (1, 2, 3)
"""
# Using a pair of parentheses to denote the empty tuple: ()
tup1 = ()

# Using a trailing comma for a singleton tuple
tup2 = (50,)
tup3 = 50,
print(isinstance(tup3, tuple))


# zip function, Returns an iterator of tuples

x = [1, 2, 3]
y = [4, 5, 6]
z = zip(x, y)
print(z)  # <zip object at 0x00000222B3935EC8>

for (x2, y2) in z:
    print(x2, y2)



# enumerate function, returns a tuple containing a count 
m = [4, 5, 6]
n = enumerate(m)
print(n)  # <enumerate object at 0x0000028EA9CA35E8>

for k, v in n:
    print(k, v)