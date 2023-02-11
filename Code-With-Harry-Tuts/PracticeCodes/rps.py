import random
import fontstyle as fnt
import os

os.system('cls')


def RPS():

  number_of_turns = 10
  options = ['Rock', 'Paper', 'Scissors']

  upoint = 0
  cpoint = 0
  turns = 1
  while (turns <= number_of_turns):
    try:
      user = int(
        input(
          fnt.apply("Enter 1 for Rock || 2 for Paper || 3 for Scissors: ",
                    "blue/bold")))
    except (TypeError, ValueError):
      continue

    computer = random.choice(options)

    if computer == 'Rock':

      if user == 1:
        print(fnt.apply("None of you got a point.", "cyan/bold"))

      elif user == 2:
        print(fnt.apply("You got a point!", 'green/bold'))
        upoint += 1

      elif user == 3:
        print(fnt.apply("Compouter got a point!", "red/bold"))
        cpoint += 1

    elif computer == 'Paper':
      if user == 2:
        print(fnt.apply("None of you got a point.", "cyan/bold"))

      elif user == 3:
        print(fnt.apply("You got a point!", 'green/bold'))
        upoint += 1
        print(fnt.apply(f'Computer: {cpoint} || User: {upoint}',
                        'yellow/bold'))
      elif user == 1:
        print(fnt.apply("Compouter got a point!", "red/bold"))
        cpoint += 1

    else:
      if user == 3:
        print(fnt.apply("None of you got a point.", "cyan/bold"))

      elif user == 1:
        print(fnt.apply("You got a point!", 'green/bold'))
        upoint += 1

      elif user == 2:
        print(fnt.apply("Compouter got a point!", 'red/bold'))
        cpoint += 1

    print(fnt.apply(f'Computer: {cpoint} || User: {upoint}', 'yellow/bold'))
    print(fnt.apply(f'Turn {number_of_turns - turns}', 'white/bold'))
    turns += 1


RPS()
