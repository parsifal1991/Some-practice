# Bemenet bekérése
n = int(input("Add meg a vizsgálni kívánt számot: "))

# Oszthatóság vizsgálata az intervallum minden elemére
def oszthatóság(n):
    intervalum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in intervalum:
        if n % i != 0:
            return False
    return True

# Eredmény kiírása
print(oszthatóság(n))