#signlie line comment
"""multi line comment"""

""" 
multi
line
comment
"""
# You can also use ctrl + / for converting a line into a comment!
# You can also use ctrl + / for converting a line into a comment!
# You can also use ctrl + / for converting a line into a comment!
# You can also use ctrl + / for converting a line into a comment!

print("For merging two print statements, you can simpleily use the end function.", end = " ")
print("Thus, I merged these two print statements")
print("You can type anything in the end function.")

print("This also", "Works!")

print("C;\\Krishna") #\\ is used to print \
print("\"Hello\"") #\" is used to print "

#\n is a new line character
#\t adds a tab  
#\r is known as carriage return
#/b is used to remove characters on the LHS(or on the left hand side of /b). But \b also requires a character on the RHS(or on the ride hand side of \b).

print("Hi\nBye")
print("Hello\tBollo") #in vscode, the size of tab is set to 8 characters by default

print("Hello\tWorld".expandtabs(tabsize = 10)) #with the 'expandtabs' function, you can increase the number of characters for one tab

print("1234567890\rABCD") #in this case, as you can see, that ABCD contains a total of 4 characters which will be replaced by the first 4 characters of the text written before \r

print("1234567890\bHi") #here, since we have used only one \b, only 0(on character written before \b) is removed.

print("1234567890\b\b\b\b\bbackspace") #here we have used 5 \b characters. Thus, the first five characters starting from the first \b on the LHS is removed.

print("12345\f67890")
print("12345\n67890")


