import fontstyle
import os

os.system('cls') # clears the screen
text = str(input(fontstyle.apply('Please Enter the text which you want to reverse: ', 'purple/bold'))) # asking the user for text
reversed_text = (text[::-1]) # reversing the text
print(fontstyle.apply(reversed_text, 'cyan/bold')) #prints the reversed text with style
