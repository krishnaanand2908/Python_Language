import os
import datetime
import fontstyle as fnt

def getdate():
    return datetime.datetime.now()

def get(name_num):
    option = input(fnt.apply('Enter 1 for excercises and 2 for food:  ', 'blue/bold'))
    if option == '1':
        content = input(fnt.apply('Enter the excercise you did:  ', 'blue/bold'))
        with open(f'{name_num}-exercise', 'a') as a:
            a.write(f'[{getdate()}]  {content}')
        print(fnt.apply('Successfully added!', 'green/bold'))
    elif option == '2':
        if option == '1':
            content = input(fnt.apply('Enter the food you ate:  ', 'blue/bold'))
            with open(f'{name_num}-diet', 'a') as a:
                a.write(f'[{getdate()}]  {content}')
            print(fnt.apply('Successfully added!', 'green/bold'))

def retrieve(name_num):
    option = input(fnt.apply('Enter 1 for excercises and 2 for food:  ', 'blue/bold'))
    if option == '1':
        name_num =  f'{name_num}'
        with open(f'{name_num}-exercise') as b:
            print(b.read())
  
    elif option == '2':
        name_num =  f'{name_num}'
    if option == '1':
            with open(f'{name_num}-diet') as b:
                print(b.read())

if __name__ == '__main__':
    print("health management system: ")
    a=int(input(fnt.apply("Press 1 for log the value and 2 for retrieve ", 'blue/bold')))

    if a==1:
        b = (input(fnt.apply('Enter the name of patient:   ', 'blue/bold')))
        get(b)
    else:
        b = (input(fnt.apply('Enter the name of patient:   ', 'blue/bold')))
        retrieve(b)
  
            