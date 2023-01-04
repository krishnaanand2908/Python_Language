# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(a, *b, **c):
    print(a)
    for item in b:
        print(c, item)
        
    
# function_name_print('Harry', "Rohan", 'Skillf', "Hammad", 'Shivam')

har = ['Harry', "Rohan", 'Skillf', "Hammad", 'Shivam', 'The Programmer', ]
var = {"NAMESTE":"USER"}
funargs(32, *har, **var)