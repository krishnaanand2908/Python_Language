import os
import math
import fontstyle
import random

def infinity_add():
	os.system('clear')
	txtadd=fontstyle.apply(f'Enter a rational number:\n', 'cyan/bold')
	disclaimer=fontstyle.apply('You can add only 2 numbers at a time', 'red/bold')
	continuetxt=fontstyle.apply('Press ENTER to add another Rational Number', 'white/bold')
	program_finished = fontstyle.apply('Program sucessfuly closed', 'green/bold')
	print(f'{disclaimer}\n')
	num1 = float(input(txtadd))
	num2 = float(input(txtadd))
	os.system('clear')
	sumtxt = (num1 + num2)
	print(fontstyle.apply(f'{num1} + {num2} = {sumtxt}', 'yellow/bold'))
	while(True):
		choice = input(continuetxt)
		if choice == '':
			numx = float(input(txtadd))
			os.system('clear')
			print(disclaimer)
			print(fontstyle.apply(f'{sumtxt} + {numx} = {sumtxt+numx}\n', 'yellow/bold'))
			continue
		else:	
			print(program_finished)	
			break

	
	
	
infinity_add()
	