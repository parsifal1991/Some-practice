nevek = ["Anna", "Béla", "Csaba"]
jegyek = [[5, 5, 4], [3, 4, 2], [5, 5, 5]]

def process_grades(nevek, jegyek):
    eredmeny = {}

    for nev, jegy in zip(nevek, jegyek):
        összeg = sum(jegy)
        darabszám = len(jegy)
        atlag = összeg / darabszám

        eredmeny[nev] = round(atlag, 2)

        if atlag >= 4.75 and all(j >= 4 for j in jegy):
            print("Kitűnő:", nev)

    return eredmeny

print(process_grades(nevek, jegyek))