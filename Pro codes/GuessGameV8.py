import random
import os
import fontstyle
import pyttsx3
import speech_recognition as sr 
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    


def wishMe2():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING, MAADHAV!...")
        
        
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTERNOON,  MAADHAV!...")
        print(fontstyle.apply(f'Good afternoon Madhav!', 'blue/bold'))
        
    elif hour == 12:
        speak("Good NOON, MAADHAV!...")
        print(fontstyle.apply(f'Good noon Madhav!', 'blue/bold'))
        
    else:
        speak(f"GOOD EVENING, MAADHAV!...")
        print(fontstyle.apply(f'Good evening Madhav!', 'blue/bold'))
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"GOOD MORNING, {name}...")
        
        
    elif hour >= 12 and hour < 18:
        speak(f"GOOD AFTERNOON,  {name}...")
        print(fontstyle.apply(f'Good afternoon {name}', 'blue/bold'))
        
    elif hour == 12:
        speak("Good NOON, {name}...")
        print(fontstyle.apply(f'Good noon {name}', 'blue/bold'))
        
    else:
        speak(f"GOOD EVENING, {name}...")
        print(fontstyle.apply(f'Good evening {name}', 'blue/bold'))
        
        
def guess_game_v5():
    os.system("CLS")
    num = 18#random.randint(1, 100)
    guess = 1
    print(fontstyle.apply("You have to guess a number between 1 to 100\nYou will only get 9 chances!\n Enjoy :-)", "Cyan/bold"))
    speak("You have to guess a number between 1 to 100... You will only get 9 chances!... ENJOY!.........")
    
    
    while (guess<=9):
        guessed_number = int(input(fontstyle.apply("Enter the number:\n", "Purple/bold")))
        if guessed_number == num:
            congo = fontstyle.apply("Congratulations!\nYou have guessed the number!", "bold/italic/white/yellow_bg/white/underline")
            print(congo)
            speak("Congratulations!!!... You have guessed the number!!!...")
            print((fontstyle.apply(f"You took {guess} turns!", "red/bold")))
            speak(f"You took {str(guess)} turns!...")
            speak("Thank Mr. Krishna Anand for creating me... You should press Enter if you want to continue...")
            print("Thank Mr. Krishna Anand for creating me. You should press Enter if you want to continue.")
            tempr = input()
            guess = guess + 1
            break
        
        elif guessed_number < num:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", "white/bold"))
            speak(f"{str(9-guess)} number of turns are left...")
            smaller = fontstyle.apply("The number you have entered is smaller than the number to be guessed!", "bold/italic/blue")
            print(smaller)
            speak("The number you have entered, is smaller... than the number to be guessed!...")
            guess = guess + 1
            continue
        
        elif guessed_number > num:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", 'white/bold'))
            speak(f"{str(9-guess)} number of turns are left...")
            greater = fontstyle.apply("The number you have entered is greater than the number to be guessed!", "bold/italic/red")
            speak("The number you have entered, is greater... than the number to be guessed!...")
            print(greater)
            guess = guess + 1
            continue 
        
        else:
            exit()
            
    if guess > 9:
        lose = fontstyle.apply("Game Over!", "bold/italic/yellow")
        print(lose)
        speak("GAME... OVER...")
        print(fontstyle.apply(f"The number was {num}", "blue/bold/underline"))
        speak("The number was {str(num)}...")
        input(fontstyle.apply("Press Enter to continue:\n", "blue/bold"))
        speak("Press ENTER to continue... my dear looser...")
        tempr = input()
            
if __name__ == "__main__":
    while True:
        os.system('cls')
        print(fontstyle.apply("Gathering Information...", "blue/bold"))
        speak("Gathering Information...")
        print(fontstyle.apply("Opening Guess Game version 8.0", "blue/bold"))
        speak("Opening Guess Game version 8.0...")
        print(fontstyle.apply("Clearing THE SCREEN...", 'blue/bold'))
        speak("Clearing the SCREEN...")
        # print(fontstyle.apply("Three...", 'blue/bold'))
        # speak("In three...")
        # print(fontstyle.apply("Two...", 'blue/bold'))
        # speak("two...")
        # print(fontstyle.apply("ONE", 'blue/bold'))
        # speak("ONE")
        
        
        
        os.system("CLS")
        
        speak("HI, It's PARTH!...")
        print(fontstyle.apply("HI, it's PARTH!", 'blue/bold'))
        speak("Type your name, USER...")
        name = input(fontstyle.apply("--->   ", 'blue/bold'))

        if name == "Krishna Anand":
            print(fontstyle.apply("Special user detcted.", 'blue/bold'))
            speak("Special User dected!...")
            wishMe2()
        else:
            wishMe()
        choice_colour = fontstyle.apply("Press Enter to continue or Q to quit!", "bold/italic/green/underline")
        print(choice_colour)
        speak("Press Enter to continue or Q to quit!... ")
        choice = input()
        choice = choice.upper()
        if choice == "":
            try:
                guess_game_v5()
            except ValueError:
                print(fontstyle.apply('An Error occured||Please Try Again', 'red/bold/underline'))
                speak("AN ERROR OCCURED... PLEASE TRY AGAIN...")
                temp = input(fontstyle.apply('Press Enter to reset the game[No Other Choice HAHA]', 'purple/bold/underline'))
                continue
        elif choice == "Q":
            bye = fontstyle.apply("|---Please come again soon---|", "bold/italic/white/red_bg")
            print(bye)
            speak("Please Come Again Soon...")
            exit()
        else:
            print()
