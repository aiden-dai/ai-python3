"""
Use x = []
"""

x = [1, 2, 3]
print(x[-1])  # 3
print(x[:-1])  #  this equals to x[:2], output: [1, 2]
print(x[::2])  # List[start:stop:stride], output: [1, 3]
print(len(x))  # 3
print(x)  # [1, 2, 3]

print(x.pop())  # pop x[-1], 3
print(x.pop(0))  # pop x[0], 1
print(x)  # [2]


y = [2, 3, 4]
y.reverse()
print(y)  # [4, 3, 2]

z = [i**2 for i in range(4)]
print(z)  # [0, 1, 4, 9]



# List Comprehensions

l1 = list(map(lambda x: x**2, range(10))) 
l2 = [x**2 for x in range(10)]
l3 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(l1)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(l2)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(l3)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

l4 = [row for row in matrix]
l5 = [[row[i] for row in matrix] for i in range(4)]
print(l4)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(l5)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]




# del list
x = [1, 2, 3, 4, 5, 6]
del x[0]
print(x)  # [2, 3, 4, 5, 6]
del x[2:3]
print(x)  # [2, 3, 5, 6]
del x[:]
print(x)  # []

