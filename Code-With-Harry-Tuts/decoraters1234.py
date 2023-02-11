# def func1():
#     print('Hello')
    
# func2 = func1
# # del func1
# func2()
# # print(id(func2))
# # print(id(func1))

# def funcret(num):
#     if num == 0:
#         return print
#     if num ==1:
#         return sum

# a = funcret(0)
# b = funcret(1)
# print(a)
# print(b)

# def executor(func):
#     func("this")
    
# executor(int)
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executung now")
        func1()
        print("Executed")
    return nowexec


@dec1
def who_is_harry():
    print("Harry is a good boy")


# who_is_harry =  dec1(who_is_harry)
who_is_harry()