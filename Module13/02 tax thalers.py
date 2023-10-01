income = float(input("Your annual income: "))

if income <= 84528:
    tax = (income * 18 / 100) - 556.2
else:
    tax = (income - 85528)* 32 / 100 + 14839.2

if tax < 0.0:
    tax = 0.0
else:
    tax = round(tax, 0)

print("Your tax is ", tax)