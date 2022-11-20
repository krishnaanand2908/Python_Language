var1 = ("Hello World ") #here var1 is a variable...it contains Hello World (string)

var2 = 7 #here var2 is also a variable...it contains 7 (integer)

var3 = 1.5 #here var3 is also a variable...it contains 1.5 (float point)

var4 = (", I am Krishna Anand") #here var4 is also a variable...it contains , I am Krishna Anand (string)

print(var1) #here we are printing var1 i.e. we are printing Hello World

print(var2) #here we are printing var2 i.e. 7

print(var3) #here we are printing var3 i.e. 1.5

print(type(var1)) #type() is an inbuilt function which tells the datatype of any variable
print(type(var2))
print(type(var3))  

print(var2 + var3) #since var2 is an integer and var3 is a floating point number, we can do mathematical operations with them.
try:
    print(var1 + var2)
except TypeError:
    print("We can't do mathematical operations with var1(string) and var2(integer)")
    print("Same for var1 and var3")
print(var1 + var4) #we can add strings to make am bigger string

var5 = ("12")
var6 = ("21")

print(int(var1) + int(var2)) #here int() is a function which can turn any string or floating point number into an integer

print(float(var1) + float(var2)) #here float() is a function which can turn any string or float into an floating point number
