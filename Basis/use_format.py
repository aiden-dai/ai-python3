# Reference:
# https://docs.python.org/3/library/string.html#formatspec

# format numbers

fa = 123.45678
print(format(fa, '0.2f'))  # 123.46
print('%0.2f' % fa)  # 123.46
print('{:.2f}'.format(fa))  # 123.46



# padding
n = 3
m = 3.5
print('{:>2d}'.format(n))  # ' 3'
print('{:0>2d}'.format(n))  # 03
print('{:0>10.1f}'.format(m))  # Right justified in 10 chars. Output: 00000003.5
print('{:0<10.1f}'.format(m))  # Left justified in 10 chars. Output: 3.50000000
print('{:0^10.1f}'.format(m))  # Left justified in 10 chars. Output: 0003.50000

print('%10.2f' % m)  # Output: '      3.50',  %0>10.2f is not supported.


x = 11
# bin() Convert an integer number to a binary string prefixed with “0b”
print(format(x, 'b'))  # 1011
print(bin(x))  # 0b1011

# oct(x) Convert an integer number to an octal string prefixed with “0o”
print(format(x, 'o'))  # 13
print(oct(x))  # 0o13

# hex(x) Convert an integer number to a lowercase hexadecimal string prefixed with “0x”
print(format(x, 'x'))  # b
print(hex(x))  # 0xb


print(int('1011', 2))  # 11
print(int('13', 8))  # 11
print(int('b', 16))  # 11
