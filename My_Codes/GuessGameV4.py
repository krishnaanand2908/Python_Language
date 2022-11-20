import random
import os
    
def guess_game():
    num = random.randint(1, 151)
    guess = 1
    print("You have to guess a number between 1 to 150\n Remember: You will get only 9 turns!")
    
    while(guess<=9):
        numg = int(input("Enter the number:\n"))
        
        if numg > num:
            print("Turns left:", 10 - guess, "--- Turn:", guess)
            print("The number you have entered is greater than the number to be guess!")
            guess = guess + 1
            continue
        elif numg < num:
            print("Turns left:", 10 - guess, "--- Turn:", guess)
            print("The number you have entered is lesser than the number to be guess!\n Try again:")
            guess = guess + 1
            continue
        else:
            print("Congratulations!\n You have guessed the the number!\n You took", guess, "number of turns to guess", num)
            input("Press Enter to continue")
            guess = guess + 1
            
            
    if guess == 10:
        print("\tGame Over!\n The number was", num)
        
while True:
    os.system("CLS")
    choice1 = input("Press Enter to continue or Q to quit:\n")
    choice1 = choice1.upper()
    
    if choice1 == "":
        guess_game()
    elif choice1 == "Q":
        exit()
    else:
        print("???")
    
        
    
    
        
        

    