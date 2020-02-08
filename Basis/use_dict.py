"""
Use x = {key: value}
x = dict([(key, value)])
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

if keys are string:
dict(sape=4139, guido=4127, jack=4098)

"""


x = {'a': 1, 'b': 2, 'c': 3}

print(x['a'])  # 1

print(x.get('a'))  # 1
print(x.get(1))  # None
print(x.get(1, 2)) # output: 2,  2 is the default value if key is not found.


print(x) # {'a': 1, 'b': 2, 'c': 3}

x.pop('a') 
print(x)  # {'b': 2, 'c': 3}

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary
print(list(x))  # ['b', 'c']
print(sorted(x))  # list in sorted order by keys, output: ['b', 'c']

x.clear() # => clear all the key-values
print(x)  # {}


# dict comprehensions
d1 = {x: x**2 for x in (2, 4, 6)}
print(d1)  # {2: 4, 4: 16, 6: 36}

# dict.items(), dict.keys(), dict.values()
for k, v in d1.items():
    print('{} = {}'.format(k, v))
