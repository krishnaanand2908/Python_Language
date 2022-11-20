import os
import fontstyle

def infinity_add():
	os.system('cls')
	txtadd=fontstyle.apply(f'Enter a rational number:\n', 'cyan/bold')
	disclaimer=fontstyle.apply('You can only add 2 numbers at a time', 'red/bold')
	continuetxt=fontstyle.apply('Press ENTER to add another Rational Number', 'white/bold')
	program_finished = fontstyle.apply('Program sucessfuly closed', 'green/bold')
	print(f'{disclaimer}\n')
	num1 = float(input(txtadd))
	num2 = float(input(txtadd))
	os.system('cls')
	sumtxt = (num1 + num2)
	print(fontstyle.apply(f'{num1} + {num2} = {sumtxt}', 'yellow/bold'))
	while(True):
		choice = input(continuetxt)
		if choice == '':
			numx = float(input(txtadd))
			os.system('cls')
			print(disclaimer)
			print(fontstyle.apply(f'{sumtxt} + {numx} = {sumtxt+numx}\n', 'yellow/bold'))
			continue
		else:	
			print(program_finished)	
			break

def infinity_subtract():
    os.system('cls')
    txtsub = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to add another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only subtract 2 numbers at a time', 'red/bold')
    print(disclaimer)
    print(fontstyle.apply('Format: [First Number] - [Second Number]', 'red/bold/underline'))
    num1 = float(input(txtsub))
    num2 = float(input(txtsub))
    difftxt = (num1 - num2)
    print(fontstyle.apply(f'{num1} - {num2} = {difftxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            numx = float(input(txtsub))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply('Format: [First Number] - [Second Number]', 'red/bold/underline'))
            print(fontstyle.apply(f'{difftxt} - {numx} = {difftxt-numx}\n', 'yellow/bold'))
            continue
        else:
            break
        
def infinity_multiply():
    os.system('cls')
    txtmulti = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to multiply another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only multiply 2 numbers at a time', 'red/bold')
    print(disclaimer)
    num1 = float(input(txtmulti))
    num2 = float(input(txtmulti))
    multitxt = (num1 * num2)
    print(fontstyle.apply(f'{num1} x {num2} = {multitxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            print(disclaimer)
            numx = float(input(txtmulti))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply(f'{multitxt} x {numx} = {multitxt*numx}\n', 'yellow/bold'))
            multitxt = numx * multitxt
            continue
        else:
            break

def infinity_divide():
    os.system('cls')
    txtdiv = fontstyle.apply('Enter a rational number:\n', 'cyan/bold')
    continuetxt=fontstyle.apply('Press ENTER to divide another Rational Number', 'white/bold')
    disclaimer=fontstyle.apply('You can only divide 2 numbers at a time', 'red/bold')
    print(disclaimer)
    print(fontstyle.apply('Format: [First Number] / [Second Number]', 'blue/bold'))
    num1 = float(input(txtdiv))
    num2 = float(input(txtdiv))
    divtxt = (num1 / num2)
    print(fontstyle.apply(f'{num1} / {num2} = {divtxt}', 'yellow/bold'))
    while(True):
        choice = input(continuetxt)
        if choice == '':
            print(disclaimer)
            numx = float(input(txtdiv))
            os.system('cls')
            print(disclaimer)
            print(fontstyle.apply('Format: [First Number] / [Second Number]', 'blue/bold'))
            print(fontstyle.apply(f'{divtxt} / {numx} = {divtxt/numx}\n', 'yellow/bold'))
            divtxt = divtxt / numx
            continue
        else:
            break    

def factorial():
     while(True):
        os.system('cls')
        inp = int(input(fontstyle.apply('Enter the number of which you want the factorial:\n', 'cyan/bold')))
        fact = 1
        if inp < 0:
            print(fontstyle.apply('Plese ENTER a Whole Number!\nPress Enter to Continue!\n', 'red/bold/underline'))
            temp = input()
            continue
        else:
            for i in range (1, inp+1):
                fact = fact*i
            print(fontstyle.apply(f'{inp}! = {fact}', 'yellow/bold'))
            
        choice = input(fontstyle.apply('Press Enter to contine else press any key:\n', 'cyan/bold'))
        if choice == '':
            continue
        else:
            break
        
factorial()