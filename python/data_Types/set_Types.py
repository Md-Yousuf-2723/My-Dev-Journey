# Set
# - Mutable
# - Unordered 
# - Doesn't allow duplicates
numbers = {1, 1, 2}
print(numbers) # Output : {1, 2}

numbers2 = {1, 2, 3, 4, 5, 6}
numbers2.add(7) # {1, 2, 3, 4, 5, 6, 7} --> 7 is added in last
print(numbers2)
numbers2.remove(2)
print(numbers2) # {1, 3, 4, 5, 6, 7}

# Frozen set
# - Immutable : cannot add or remove elements.
number_froz = frozenset([1, 2, 3, 4])
print(number_froz)
print(type(number_froz))