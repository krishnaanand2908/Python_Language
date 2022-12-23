# Pattern Printing
# Input = an integer 'n'
import os

os.system('cls')

while 1:
    n = int(input('Enter the number of rows:  '))
    pattern_type = int(input('Enter 1 to print the start pattern in ascending form or enter 2 to print it in descending form:  '))
    if pattern_type == 1:
        pattern_type = True
    elif pattern_type == 2:
        pattern_type = False
    else:
        print('Get Lost!')

    if pattern_type == True:
        for i in range(1, n+1, 1):
            print('*'*i)
    elif pattern_type == False:
        for i in range(n+1, 1, -1):
            print('*'*i)
        print('*')

