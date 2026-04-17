import math

a = float(input("Adja meg az 'a' oldalt (legfeljebb 30):"))
b = float(input("Adja meg a 'b' oldalt (legfeljebb 30):"))

if a > 30:
    print("Oldalhossz max. 30 lehet!")
elif b > 30:
    print("Oldalhossz max. 30 lehet!")
else:
    c = math.sqrt(a**2 + b**2)
    print(f"Adja meg az 'a' oldalt (legfeljebb 30): Adja meg a 'b' oldalt (legfeljebb 30): A háromszög átfogója: {math.ceil(c)}")

    a = int(a)
    b = int(b)
    
    for i in range(1, a + 1):
        csillagok = math.ceil(i * (b / a))
        print("*" * csillagok)