# Sequence type - List
# - Mutable
# - Use more memory
# - Slower
# - Syntax : []
fruits = ["", "Banana", "Mango"]
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
print(coordinate(0), )