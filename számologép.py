import math

operator = input("Enter an operator(+ - * /: )")

num1 = float(input("Adja meg az első számot: "))
num2 = float(input("Adja meg a második számot: "))

if operator == "+":
    result = num1 + num2
    print (round(result))
elif operator == "-":
    result = num1-num2
    print(round(result))
elif operator == "/":
    result = num1/num2
    print(round(result))
elif operator == "*":
    result = num1*num2
    print(round(result))
else:
    print(f"{operator}is not valid operator!")