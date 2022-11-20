import os
os.system('cls')

# grocery = ['Harpic', 'vim bar', 'deodrant', 'Bhindi', 'Lollypop', '56']
# print(grocery)

# print(grocery[0]) # Harpic is on index no. 0
num = [2, 7, 9, 11, 3]
print(num)
print(num[2]) 

num.sort() # this function is used to sort numbers in a list weather they are floating points numbers or integers from the lowest to the highest

print(num)

num.reverse() # this function is used to print number in a list from greatest to smallest

print(num)

"""
We can use slicing in lists too
"""
# print(max[num])
# print(min[num])

# list.append() is a function which adds items at the end of a list
# list.pop() removes items from the end of a list
# list.insert() inserts items anywhere you wants in a list

# Mutable- can be changes  Immutable- cannot be changed
# List is mutable  Touple cannot be changed

touple = (1, 2, 3, 4, 5) # If we try to change it, we will get an error
"""Swap Variable Contents"""
 
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)



