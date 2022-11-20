import os
import fontstyle

os.system("cls")

def Zpattern():
    txt = fontstyle.apply(f"Enter the number of starts for Z pattern\n", "bold/underline/yellow")
    n = int(input(txt))
    for i in range(n):
        if i == 0 or i == n-1:
            print("*"*n)
        else:
            for j in range(n-1-i):
                print(" ", end="")
            print("*", end="")
            for k in range(n-i, n):
                print(" ", end="")
        print("\n")


while(True):
    try:
        Zpattern()
    except (ValueError, OverflowError):
        ign = fontstyle.apply(f"Retry\n", "italic/black/")
        print(ign)
    inptxt = fontstyle.apply(f"Press Enter to continue:\n", "Green/bold")
    inp = input(inptxt)
    os.system("cls")
    continue
    