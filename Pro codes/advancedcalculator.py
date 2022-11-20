import os
import math


def basic_calc():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opr = input("Enter operation: {+, -, /, *, %}: ")

    if opr == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif opr == '-':
        print(f"{num1} - {num2} = {num1-num2}")
    elif opr == '*':
        print(f"{num1} x {num2} = {num1*num2}")
    elif opr == '/':
        print(f"{num1} {chr(247)} {num2} = {num1/num2}")
    elif opr == '%':
        print(f"{num1} %% {num2} = {num1%num2}")


def advance_hcf():  # hcf and gcd are same thing
    list1 = []  # Empty list to store all hcf elements
    while True:
        element = input(
            "Enter integer element or press Enter to display result: ")
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_gcd = list1[0]  # assumed first element of list as gcd
    for i in list1:
        # comparing gcd with every element if list
        temp_gcd = math.gcd(temp_gcd, i)

    print("HCF of {", end="")  # printing the hcf
    for x in list1:
        print(f"{x}, ", end="")
    print("} = ", temp_gcd)


def advance_lcm():
    list1 = []  # Empty list to store all hcf elements
    while True:
        element = input(
            "Enter integer element or press Enter to display result: ")
        if element == "":  # checks if user has entered "ENTER"
            break  # exit the while loop
        else:
            element = int(element)  # converting string element into integer
            list1.append(element)  # adding element to list

    temp_lcm = list1[0]  # assumed first element of list as lcm
    for i in list1:
        # comparing lcm with every element if list
        temp_lcm = math.lcm(temp_lcm, i)

    print("LCM of {", end="")  # printing the lcm
    for x in list1:
        print(f"{x}, ", end="")
    print("} = ", temp_lcm)


def advance_calc():
    choice = int(input("1.HCF\n2.LCM\n...> "))
    if choice == 1:  # HCF or GCD code
        advance_hcf()
    elif choice == 2:
        advance_lcm()


def exponential_calc():
    base = float(input("Enter base value: "))
    power = float(input("Enter power value: "))
    print(f"{base} raised to {power} is {pow(base, power)}")


def multiplication_tables():
    num = int(input("Enter number of which multiplication table is required: "))
    multiple = int(input("Enter number of multiples required: "))
    for i in range(1, multiple+1):
        print(f"{num} x {i} = {num*i}")


def exponential_table():
    try:  # used this to handle overflow error which is very common in exponents
        base = float(input("Entervalue for initial base: "))
        power = float(input("Enter power value: "))

        for i in range(10):
            print(f"S.No{i+1}   {base} raised to {power} is {pow(base, power)}")
            temp = pow(base, power)  # new base
            base = temp  # storing new base in base variable

    except OverflowError:  # results too large
        print("\nUnable to print further results.\nResult too large.\nSORRY!!!")


if __name__ == '__main__':
    while True:
        os.system("cls")
        choice1 = int(input(
            "1.Basic Calculator\n2.Advanced Calculator\n3.Exponential Calculator\n4.Multiplication Tables\n5.Exponential Table\n...> "))
        os.system("cls")

        if choice1 == 1:
            basic_calc()

        elif choice1 == 2:
            advance_calc()

        elif choice1 == 3:
            exponential_calc()

        elif choice1 == 4:
            multiplication_tables()

        elif choice1 == 5:
            exponential_table()

        else:
            print("Wrong Choice\n")

        quit = input(
            "\n\n\nIf you want to continue press enter or press Q\n...> ")
        if quit.lower() == 'q':
            exit()
