import fontstyle
import os
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    
os.system('cls')

while(True):
    query = str(input(fontstyle.apply('Search Google or type a URL:\n', 'cyan/bold')))
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(fontstyle.apply(j, 'purple/bold'))
    input()
    os.system('cls')