# Byte : Every char in str in byte. 
# H + e + l + l + o = Hello
# here  H, e, l, l, o --> byte and we can know their ascii values
# Bytes : Mutable
data = b"Hello" # b --> bytes
print(data[0]) # Output: 72 --> ASCII of H
print(data[1]) # Output : 101 --> ASCII of e
print(type(data))

# bytearray : Immatuable 
