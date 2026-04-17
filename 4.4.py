
szamok = []

while True:
    szam = input()
    if szam == "":
        break
    szamok.append(int(szam))
    
if len(szamok) < 2:
    print("Nem adott meg legalabb ket ervenyes szamot.")

else:
    
    osszeg = szamok[0] + szamok[-1]
    atlag = (szamok[0] + szamok [-1]) / 2
        
    print(f"Az elso es az utolso szam osszege: {osszeg}")
    print(f"Az elso es az utolso szam atlaga: {atlag}")