a = list(range(10))
print(a)

b = filter(lambda x: x> 5, a)
print(b)  # <filter object at 0x000001A99D6ADE48>

c = list(filter(lambda x: x> 5, a))
print(c)  # [6, 7, 8, 9]

