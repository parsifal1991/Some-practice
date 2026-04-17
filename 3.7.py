szam=int(input())
if szam<0:
    print(" A megadott szám helyetelen mivel, pozitiv számot kérünk! ")
else:
    for i in range (szam):
        szokozok=" " * (szam-1-i)
        csillagok_szama=1 + i * 2
        print(szokozok+"*" * csillagok_szama)