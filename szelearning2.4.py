szoveg = input()
uj_szoveg = ""

for betu in szoveg:
    if betu == "a":
        uj_szoveg += "4"
    elif betu == "e":
        uj_szoveg += "3"
    elif betu == "o":
        uj_szoveg += "0"
    else:
        uj_szoveg += betu

print(uj_szoveg)