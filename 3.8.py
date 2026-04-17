szam = int(input())

osszeg = 0
n = 2  # Prímeket 2-től kezdjük
primszamok = []

def prim_e(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while osszeg + n <= szam:  # Csak addig folytatjuk, amíg az összeg kisebb vagy egyenlő
    if prim_e(n):  # Ha prím
        primszamok.append(n)
        osszeg += n  # Frissítjük az összeget
    n += 1  # Következő szám

print(" ".join(map(str, primszamok)))  # Kiírjuk a prímeket