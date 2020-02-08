
# new bytes object: bytes() or b''
b1 = bytes()
b2 = b''
b3 = b'hello'

print(b3)  # b'hello'
print(b3[0])  # ?
print(b3[:4])  # b'hell'

# str to bytes
b4 = bytes('Hello World',encoding='utf-8')
b5 = "Hello World".encode('utf-8')
print(b4)
print(b5)

# bytes to str
s1 = b5.decode('utf-8')
print(s1)
print(type(s1))  # <class 'str'>