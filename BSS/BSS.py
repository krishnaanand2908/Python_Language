import os
import fontstyle
from BssFUN import *
from BssSTUDY import *

hehe = fontstyle.apply("|---Please come again soon---|", "bold/Italic/black")      

if __name__ == "__main__":

    
    os.system("cls")
    bss_logo = fontstyle.apply("Welcome to BSS!", "bold/Italic/DARKCYAN/green_BG")
    hehe = fontstyle.apply("|---Please come again soon---|", "bold/Italic/black")
    print(bss_logo)

    name = str(input("Please enter your name here:\n"))
    sex = str(input("Please enter your sex here [F\M]:\n"))
    sex = sex.upper()

    while True:
        garb = input(":::::::::::::::::::::::::::::::::::::::::Press Enter to clear the screen:::::::::::::::::::::::::::::::::::::::::")
        os.system("cls")
        if sex == "F":
            print(f"Hi Ms\Mrs. {name}!\n Please select where you want to go:\n[1. Fun Corner\n2. Study Corner]\n3.[EXIT]")
        elif sex == "M":
            print(f"Hi Mr. {name}!\n Please select where you want to go:\n[1. Fun Corner]\n[2. Study Corner]\n3.[EXIT]")
        else:
            print(hehe)
        choice = int(input())

        if choice == 1:
            print("1. Foody Table\n 2. Guess the number\n 3. Number Fight\n")
            game_choice = int(input(":"))
            if game_choice == 1:
                foody_table()
            elif game_choice == 2:
                guess_game_v5()
            elif game_choice == 3:
                num_fight()
                
        elif choice == 2:
            print("1. Calculator\n 2. Quiz\n 3. Animal's Info\n")
            study_choice = int(input(":"))
            if study_choice == 1:
                calcy()
            elif study_choice == 2:
                quizy()
            elif study_choice == 3:
                animals()
        elif choice == 3:
            print("Thankyou for visiting")
            print(hehe)
            exit()
        else:
            print(hehe)
            exit()
    


    
    
    






