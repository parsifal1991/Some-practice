számok = []
while len(számok) < 5 :
    szám = int(input("Adja meg a vizsgálni kívánt számokat:"))
    számok.append(szám)

def above_average(számok):
    megoldás = []
    számok_összege = sum(számok)
    számok_db = len(számok)
    átlag = számok_összege / számok_db
    for szám in számok:
        if szám > átlag:
            megoldás.append(szám)
    return megoldás
print(above_average(számok))