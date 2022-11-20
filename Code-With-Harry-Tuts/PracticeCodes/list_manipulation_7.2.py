import fontstyle
import os
os.system('cls')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(fontstyle.apply('Slice 1:', 'purple/bold'))
slice1 = list[5:15:2] # step = 2 because we have to skip every second item 
slice2 = list[::4] # step = 4 because we have to skip every 4th item
sum = 0
print(fontstyle.apply('Elements of Slice 1:', 'cyan'))
for i in slice1:
    sum = sum + i
    print(i, end=' ') # end=' ' helps us to add a space between all the numbers we want to print
print()
print(fontstyle.apply(f'Sum of elements in slice 1 = {sum}', 'yellow'))

print(fontstyle.apply('Slice 2:', 'purple/bold'))
sum = 0
print(fontstyle.apply('Elements of Slice 2:', 'cyan'))
for j in slice2:
    sum = sum + j
    print(j, end=' ') # end=' ' helps us to add a space between all the numbers we want to print
print()
average = sum/len(slice2) # len() function defines the length of slice2
                          # sum / len(slice2) means sum of all the elements of slice2 divided by number of elements in slice2 i.e. 45 divided by 5 which equals to 9
print(fontstyle.apply(f'Average of elements in slice 2 = {average}', 'yellow'))


    
     
