import random

def quizy():
    score = 0
    numc = random.randint(1, 8)
    
    if numc == 1:
        print("Which is the largest continent in the world?")
        print("a. Antarctica")
        print("b. Asia")
        print("c. America")
        print("d. South Australia")
        answer = input("")
        if answer == "a":
            score +=1
        
    elif numc == 2:
        print("Name the only non-metal which is found in liquid state.")
        print("a. Mercury")
        print("b. Bromine")
        print("c. Water")
        print("d. Hydroxide")
        answer = input("")
        if answer == "b":
            score +=1
            
    elif numc == 3:
        print("Name the only metal which is found in liquid state.")
        print("a. Mercury")
        print("b. Molten Magma")
        print("c. Molten Iron")
        print("d. Liquisteel")
        answer = input("")
        if answer == "a":
            score +=1
            
    elif numc == 4:
        print("Which of the following is a semiaquatic mammal?")
        print("a. Killer Whale")
        print("b. Tiger Shark")
        print("c. Hippopotamus")
        print("d. both a and b ")
        answer = input("")
        if answer == "c":
            score +=1
            
    elif numc == 5:
        print("Which of the following trees have roots above the ground?")
        print("Mango Tree")
        print("b. Spade cactus")
        print("c. Mangrove tree")
        print("d. there's no tree which grow roots above the ground")
        answer = input("")
        if answer == "c":
            score +=1
            
    elif numc == 6:
        print("Who discovered the vaccine for small pox?")
        print("a. Poxes Vacenito")
        print("b. Galileo Galilei")
        print("c. Edward Jenner")
        print("d. Louis Pasteur")
        answer = input("")
        if answer == "c":
            score +=1
            
    elif numc == 7:
        print("Wine is made from __")
        print("a. grapes")
        print("b. alchohol")
        print("c. Whisky")
        print("d. mango")
        answer = input("")
        if answer == "a":
            score +=1
        
    # if numc == 1 and answer == "b":
    #     right = ("Y")
    #     score += 1
    # elif numc == 2 and answer == "b":
    #     right = ("Y")
    #     score += 1
    # elif numc == 3 and answer == "a":
    #     right = ("Y")
    #     score += 1
    # elif numc == 4 and answer == "c":
    #     right = ("Y")
    #     score += 1
    # elif numc == 5 and answer == "c":
    #     right = ("Y")
    #     score += 1
    # elif numc == 6 and answer == "c":
    #     right = ("Y")
    #     score += 1
    # elif numc == 7 and answer == "a":
    #     right = ("Y")
    #     score += 1
    # else:
    #     score+=0
    return score
        
    
round = 1
name = input("Enter your name here:\n")

while (round < 8):
    score = quizy()
    
    if round > 7:
        print(name, "scored", score, "points!")
    
    round = round + 1