# Byte : Every character in string in byte. 
# H + e + l + l + o = Hello
# here  H, e, l, l, o --> byte and we can know their ascii values
# Bytes : Mutable
data = b"Hello" # b --> bytes
print(data[0]) # Output: 72 --> ASCII of H
print(data[1]) # Output : 101 --> ASCII of e
print(data) # b'Hello'
print(type(data))

# bytearray : Immatuable 
# data2 = bytearray("python") --> bytearray can't take string
data3 = bytearray([1, 2, 3])
print(data3[0]) # 1
print(data3[1]) # 2
print(data3)