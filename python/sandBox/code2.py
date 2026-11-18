# Sequence type - List
# - Mutable
# - Use more memory
# - Slower
# - Syntax : []
fruits = ["Apple", "Banana", "Mango"]
         #  0         1         2
fruits.append("Orange") # Append adds at last of a list
# new list fruits = ["Apple", "Banana", "Mango", "Orange"]
                    #  0         1         2        3
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# List is mutable
fruits[1] = "Grapes"
# new list fruits = ["Apple", "Grapes", "Mango", "Orange"]
                    #  0         1         2        3

print("-----New list-----")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
# Printing type
print(type(fruits))
# Number list
num = [11, 22, 33]
print("-----Number list-----")
print(num[0])
print(num[1])
print(num[2])

# Sequence type - Tuple
# - Immutable
# - Use less memory
# - Faster
# Sytax : ()
coordinate = (10, 20, 30)
        #     0   1   2 
print("----Tuple----")
print(coordinate[0], coordinate[1], coordinate[2])
tuple_str = ("Man", "Woman") # tuple can hold strings
print(tuple_str[0])
print(tuple_str[1])
# Printing type
print(type(coordinate))

# Sequence type - Range
# Synatx : range(start, stop, steps)
print("----Range----")
range(1,10,1) # The range is created but can't be print
#range = [] # range can be used as variable name in list
#range = () # range can be used as variable name in Tuple
# Printing range
# Unpack
print(*range(1,10,2)) # * --> to unpack
print(*range(1,20,2), sep=", ") # sep=", " used to separeat by ','
# Convert it to list
print(list(range(1,30,3)))
# For loop
for val in range(1,40,5):
    print(val)