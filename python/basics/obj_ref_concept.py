x = 23
y = x
# Here,
# x --> 23 <-- y
# x and y pointing to same obj
print(x)
print(y)

print(x == y) # Checks if x and y values is or not
print(x is y) # Checks if x and y pointing same obj in memory or not
y = 23 # Here I explicity declared y will be pointing another obj in the memory whoes value is 23
print(x == y) # True
print(x is y) # False

# Same of List
list1 = [1, 2, 3]
list2 = list1[:] # list1 is copied to list
# Here [:] means slicing start to end
# Syntax : [start:end]
# [1,2,3,4] --> [0:2] --> [1,2] {stops before index 2}
#! pro
print(list1)
print(list2)
list1[0] = 55
print(list1)
print(list2)