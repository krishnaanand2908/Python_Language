import os
os.system('cls')

mystr = "Harry is a good boy" # here mystr is a variable which contatins a string
print(mystr[4]) # here we are slicing the string. [4] means the fifth charecter of the string because index in python starts from 0.

print(mystr[0:5]) # here we are picking a part of mystr variable by using string slicing. 0:5 means first charecter to (5-1)th charecter because python doesn't include the fifth charecter here. Same for 0:6 and 0:7, etc.

print(len(mystr)) # len() is a function which defines the length of a string. 
                  # Here the lenght of out string is 18 but since 0 is included, it will print 19.
                  
"""
suppose we type,
print(mystr[100])
the obviously it will give us the IndexError because the maximum index limit we have is 19.
"""

print(mystr[0:100]) # Programm won't give us any kind of error because the program will see the minimum and the maximum number of charectors here. I meant that here it will ignore the error and will print the whole string.

print(mystr[0:]) # no charector after colon means that the progrmam will print every charector from the first given index to the last possible index.

print(mystr[:5]) # no charector before colon means that the progrmam will print every charector from the first index to the last given index.

print(mystr[::]) # no integer after the second colon means that there is 1 because after the second colon 1 is fixed by default.

print(mystr[::2]) # it means that the program will print the contents of mystr skipping every charector one after the another.

"""Negative Index"""

print(mystr[-1::]) # negative index is the same as postive index but its just backward

# True and False are boolian charactors
"""Alpha numeric strings are strings containing 'NO SPACES' and 'NUMBERS'"""
"""Alpha strings are strings containing 'NO SPACES'"""
"""Numeric strings are strings containing 'NUMBERS'"""

#string.isalpha() tells weather the string have spaces or not
#string.isnumeric() tells weather the string have numbers or not
#string.isalnum() tells weather the string have spaces and numbers or not
#string.endswith() tells weather the given string is ending with the given argument or not
#mystr.count() tells the number of given argument in the given string
#string.capitalize() capitalizes the first charactor of the given string
#string.find() finds the given charactor in the given string
#string.lower() lowers all the charactors of the given string
#string.upper() capitalizes all the charactors of the given string
#string.replace() replaces a charactor in the place of another in the given string











