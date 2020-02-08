"""
A set object is an unordered collection of distinct hashable objects.
sets do not support indexing, slicing, or other sequence-like behavior.

The set type is mutable — the contents can be changed using methods like add() and remove(). 
Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. 
The frozenset type is immutable and hashable — its contents cannot be altered after it is created;

For example:
set('abc')
frozenset('abc')


Create:

s = {value01,value02,...}

s = set(...)


Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary
s = set()



s.add(x)
s.remove(x)
"""

s1 = set('abcdeac')
print(s1)  # {'c', 'd', 'a', 'b', 'e'}




# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.


a = set('abcde')
b = set('acf')
print(a - b)  # letters in a but not in b, output: {'b', 'e', 'd'}

print(a | b)  # letters in a or b or both, output: {'e', 'b', 'f', 'd', 'c', 'a'}

print(a & b)  # letters in both a and b, output: {'a', 'c'}

print(a ^ b)  # letters in a or b but not both, output: {'e', 'f', 'd', 'b'}


# set comprehensions

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'d', 'r'}