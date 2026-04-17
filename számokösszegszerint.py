számok = []

# 5 szám bekérése a felhasználótól
while len(számok) < 5:
    szam = int(input("Adja meg a vizsgálni kívánt számokat: "))
    számok.append(szam)

# Függvény a számjegyösszeg szerinti rendezésre
def sort_by_digit_sum(számok):
    rendezett = sorted(számok, key=lambda x: (sum(int(c) for c in str(x)), x))
    return rendezett

# Rendezett lista kiírása
print("Rendezett lista számjegyösszeg szerint:", sort_by_digit_sum(számok))