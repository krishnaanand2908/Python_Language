import random
import fontstyle as fnt
import os

os.system('cls')

def RPS():
    options = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(options)
    upoint = 0
    cpoint = 0
    turns = 0
    while(turns <= 10):
        try:
            user = int(input(fnt.apply('Enter 1 for Rock || 2 for Paper || 3 for Scissors: ', 'blue/bold')))
        except TypeError:
            continue
        
        # If Ties
        if computer == 'Rock' and user == 1:
            print(fnt.apply('TIE!', 'cyan/bold'))
        elif computer == 'Paper' and user == 2:
            print(fnt.apply('TIE!', 'cyan/bold'))
        elif computer == 'Scissors' and user == 3:
            print(fnt.apply('TIE!', 'cyan/bold'))

        # If computer chooses rock
        if computer == 'Rock':
            if user == 2:
                upoint += 1
                print(fnt.apply('You win!', 'green/bold'))
            elif user == 3:
                cpoint += 1
                print(fnt.apply('You loose!', 'red/bold'))
        elif computer == 'Paper':
            if user == '1':
                cpoint += 1
                print(fnt.apply('You loose!', 'red/bold'))
            elif user == '3':
                upoint += 1
                print(fnt.apply('You win!', 'green/bold'))
        else:
            if user == '1':
                upoint += 1
                print(fnt.apply('You win!', 'green/bold'))
            elif user == '3':
                cpoint += 1
                print(fnt.apply('You loose!', 'red/bold'))
        turns += 1
    if cpoint < upoint:
        print(f'You WON the Game by {upoint - cpoint} points!')     
    elif cpoint > upoint:
        print(f'You LOST the Game by {cpoint - upoint} points!')
    else:
        print(f'TIE Breaker occured!\n Computer scored: {cpoint}\n User scored: {upoint}')      
        
RPS()
                
                
                
        