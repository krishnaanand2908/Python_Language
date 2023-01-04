########################################MAP################################
numbers = ["3", "34", "64", True, ]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers = list(map(int, numbers))

numbers[2] = numbers[2] + 1
# print(numbers)


# def sq(a):
#     return a**2



# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# square = list(map(lambda x: x**2, num))
# print(square)

def sq(a):
    return a*a

def cu(a):
    return a**3

# funcs = [sq, cu]
# for i in range(5):
#     val = list(map(lambda x:x(i), funcs))
#     print(val)
#################################FILTER######################################
list_1 = [1,2,3,4,5,6,7,8,9]

def is_g(num):
    return num>5

gr_th_5 = list(filter(is_g, list_1))
print(gr_th_5)
##################################REDUCE########################################
from functools import reduce

num = reduce(lambda x,y: x*y, list_1)
print(num)