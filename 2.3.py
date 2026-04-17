# Szemelyi szam bekerese
szemelyi_szam = input().strip()

# Ellenorizzuk, hogy a szemelyi szam 11 szamjegy hosszú-e
if len(szemelyi_szam) == 11 and szemelyi_szam.isdigit():
    # Elso 10 szamjegy es a 11. szamjegy
    szamjegyek = [int(szemelyi_szam[i]) for i in range(10)]  # Elso 10 szamjegy
    tizenegyedik_szamjegy = int(szemelyi_szam[10])  # 11. szamjegy
    
    # Sullyok (1-tol 10-ig)
    sullyok = [i + 1 for i in range(10)]
    
    # A szorzatok osszege
    szorzatok_osszege = sum([szamjegyek[i] * sullyok[i] for i in range(10)])
    
    # Kiszamoljuk a maradekot
    maradek = szorzatok_osszege % 11
    
    # Ellenorizzuk, hogy a maradek megegyezik-e a 11. szamjeggyel
    if maradek == tizenegyedik_szamjegy:
        print("A szemelyi azonosito valodi.")
    else:
        print("A szemelyi azonosito nem valodi.")
else:
    print("A megadott azonosito nem 11 szamjegybol all.")