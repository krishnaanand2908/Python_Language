import random
import os
import fontstyle

def guess_game_v5():
    os.system("CLS")
    num = random.randint(1, 100)
    guess = 1
    print(fontstyle.apply("You have to guess a number between 1 to 100\n You will only get 9 chances!\n Enjoy :-)", "Cyan/bold"))
    
    while (guess<=9):
        guessed_number = int(input(fontstyle.apply("Enter the number:\n", "Purple/bold")))
        if guessed_number == num:
            congo = fontstyle.apply("Congratulations!\nYou have guessed the number!", "bold/italic/white/yellow_bg")
            print(congo)
            print((fontstyle.apply(f"You took {9-guess} turns!", "red/bold")))
            guess = guess + 1
            break
        
        elif guessed_number < num:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", "white/bold"))
            smaller = fontstyle.apply("The number you have entered is smaller than the number to be guessed!", "bold/italic/blue")
            print(smaller)
            guess = guess + 1
            continue
        
        elif guessed_number > num:
            print(f"Turns remaining: {9-guess}")
            greater = fontstyle.apply("The number you have entered is greater than the number to be guessed!", "bold/italic/red")
            print(greater)
            guess = guess + 1
            continue 
        
        else:
            exit()
            
    if guess > 9:
        lose = fontstyle.apply("Game Over!", "bold/italic/yellow")
        print(lose)
        print(fontstyle.apply(f"The number was {num}", "blue/bold/underline"))
        input(fontstyle.apply("Press Enter to continue:\n", "blue/bold"))
            
if __name__ == "__main__":
    while True:
        os.system("CLS")
        choice_colour = fontstyle.apply("Press Enter to continue or Q to quit!", "bold/italic/green/underline")
        print(choice_colour)
        choice = input()
        choice = choice.upper()
        if choice == "":
            try:
                guess_game_v5()
            except ValueError:
                print(fontstyle.apply('An Error occured||Please Try Again', 'red/bold/underline'))
                temp = input(fontstyle.apply('Press Enter to reset the game[No Other Choice HAHA]', 'purple/bold/underline'))
                continue
        elif choice == "Q":
            bye = fontstyle.apply("|---Please come again soon---|", "bold/italic/white/red_bg")
            print(bye)
            exit()
        else:
            print()
