
def is_armstrong(n: int) -> bool:
    eredeti = n
    szamjegyek = str(n)
    jegy_szam = len(szamjegyek)
    
    osszeg = 0
    for c in szamjegyek:
        osszeg += int(c) ** jegy_szam
    
    return osszeg == eredeti

# Bemenet bekérése
n = int(input("Add meg a számot: "))
if is_armstrong(n):
    print(f"{n} Armstrong‑szám")
else:
    print(f"{n} nem Armstrong‑szám")