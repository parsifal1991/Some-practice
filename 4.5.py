
szamok = []


for _ in range(5):
    szam = int(input(""))
    szamok.append(szam)


for _ in range(4): 
    legnagyobb = max(szamok)
    szamok.remove(legnagyobb)
    osszeg = sum(szamok)
    print(f"Legnagyobb szam eltavolitva: {legnagyobb}, maradek osszeg: {osszeg}")