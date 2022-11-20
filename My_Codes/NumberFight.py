import random
import os
import fontstyle

def num_fight():
    while True:
        os.system("CLS")
        ai = random.randint(-100, 101)
        score = 0
        player_print = fontstyle.apply("Enter your number here [from -100 to 100] [let's see who wins...]:", "bold/italic/purple")
        print(player_print)
        inp = int(input())
        
        if ai > inp:
            greater = fontstyle.apply("HEHE, You lost! [score -1]", "bold/red")
            print(greater)
            score -= 1
            print("Your opponent guessed", ai)
            input("Press Enter to continue")
            
        elif ai < inp:
            smaller = fontstyle.apply("You Won! [score  +1]", "bold/green")
            print(smaller)
            score += 1
            print("Your opponent guessed", ai)
            input("Press Enter to continue")
            
        else:
            equal = fontstyle.apple("TIE [score +0]", "bold/blue")
            print(equal)
            print("Your opponent guessed", ai)
            input("Press Enter to continue")
        
if __name__ == "__main__":
    while True:
        os.system("CLS")
        choice = fontstyle.apply("Press Enter to continue or Q to quit!", "bold/cyan")
        print(choice)
        inp1 = input(":")
        inp1 = inp1.upper()
        if inp1 == "":
            num_fight()
        elif inp1 == "Q":
            exit()
        else:
            print()
        