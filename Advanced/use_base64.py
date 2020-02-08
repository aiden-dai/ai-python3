import base64

""" Encoding """
s = 'Hello world'
s = s.encode('utf-8')
encodes = base64.b64encode(s)  # base64.b64encode(str) will run into TypeError.
print(encodes)

""" Decoding """
decodes = base64.b64decode(encodes)
print(decodes)
print(decodes is str)  # return False
print(type(decodes))  # return <class 'bytes'>
