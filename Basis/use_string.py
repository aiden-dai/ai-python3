"""
Strings are immutable sequences of Unicode code points.
"""


"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

"""

## ord() and chr()

a = '我'
b = ord(a)  # return the unicode code for one character
c = chr(b)  # return the unicode string for code
print(b)  # 25105
print(c)  # 我

def is_chinese_char(cp):
    """From Google/Bert"""
    if ((cp >= 0x4E00 and cp <= 0x9FFF) or  #
        (cp >= 0x3400 and cp <= 0x4DBF) or  #
        (cp >= 0x20000 and cp <= 0x2A6DF) or  #
        (cp >= 0x2A700 and cp <= 0x2B73F) or  #
        (cp >= 0x2B740 and cp <= 0x2B81F) or  #
        (cp >= 0x2B820 and cp <= 0x2CEAF) or
        (cp >= 0xF900 and cp <= 0xFAFF) or  #
        (cp >= 0x2F800 and cp <= 0x2FA1F)):  #
      return True

    return False


print(is_chinese_char(b))
print(is_chinese_char(ord('~')))