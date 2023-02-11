import random
import fontstyle as fnt
import os



def kbb():
  print(fnt.apply('\t\t  Kaun Banega Bhikaari!?', 'purple/bold'))
  money = 0
  i = 0
  questions = ['What is the scientific name of peacock?', 'What is the chemical formula of water/oxidane?', 'Name the largest continent according to landmass', 'What is the real name of code with harry?']

  while i > 5:
    random.shuffle(questions)
    current_question = random.choice(questions)
    
    print(fnt.apply(current_question, 'blue/bold'))
    
    ans = input(fnt.apply('Ans: ', 'yellow/bold'))
    ans = ans.lower()
    
    if current_question == questions[0] and ans == 'pava cristatus':
        print(fnt.apply('Congratulations! Your answer is right'))
        money = money + 1000
        print(fnt.apply(f'Current Amount: {money}', 'blue/bold'))
        temp=(fnt.apply('Press Enter for the next question: ', 'pink/bold'))
    elif current_question == questions[1] and ans == 'h20':
        print(fnt.apply('Congratulations! Your answer is right'))
        money = money + 1000
        print(fnt.apply(f'Current Amount: {money}', 'blue/bold'))
        temp=input((fnt.apply('Press Enter for the next question: ', 'pink/bold')))
    elif current_question == questions[2] and ans == 'asia':
        print(fnt.apply('Congratulations! Your answer is right'))
        money = money + 1000
        print(fnt.apply(f'Current Amount: {money}', 'blue/bold'))
        temp=input((fnt.apply('Press Enter for the next question: ', 'pink/bold')))
    elif current_question == questions[3] and ans == 'haris ali khaan':
        print(fnt.apply('Congratulations! Your answer is right'))
        money = money + 1000
        print(fnt.apply(f'Current Amount: {money}', 'blue/bold'))
        temp=input((fnt.apply('Press Enter for the next question: ', 'pink/bold')))
    else:
        print(fnt.apply('Your answer is wrong!\nGAME OVER!', 'red/bold/underline'))
        temp=input((fnt.apply('Press Enter for the next question: ', 'pink/bold')))
    i += 1
    


    
if __name__ == '__main__':
  os.system('clear')
  input(fnt.apply('Press Enter to start the KBB game!\n--->  ', 'white/bold'))
  os.system('clear')
  kbb()
  