def whole_square():
    a = float(input('Enter first number:\n'))
    b = float(input('Enter second number:\n'))
    wholesq = (a**2) + (b**2) + (2*a*b)
    print(f"({a}+{b})^2 = {wholesq}")
whole_square()