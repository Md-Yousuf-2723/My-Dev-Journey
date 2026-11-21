x = 23
y = x
# Here,
# x --> 23 <-- y
# x and y pointing to same obj
print(x)
print(y)

print(x == y) # Checks if x and y values is or not
print(x is y) # Checks if x and y pointing same obj in memory or not
y = 23 # Here I explicity declared y will be pointing another obj in the memory 