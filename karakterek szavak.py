mondat = input("Adja meg a vizsgálni kívánt mondatot: ")
karakterek_száma = [] 
nagybetűs = 0
kisbetűs = 0

for karakter in mondat:
    karakterek_száma.append(karakter)
    if karakter.isupper():
        nagybetűs += 1
    elif karakter.islower():
        kisbetűs += 1

szavak = mondat.split()
leghosszabb_szó = max(szavak, key=len)

print("Kisbetűs karakterek száma:", kisbetűs)
print("Nagybetűs karakterek száma:", nagybetűs)
print("A leghosszabb szó:", leghosszabb_szó)
print("Szavak darabszáma:", len(szavak))
print("Karakterek száma szóközökkel:", len(karakterek_száma))
print("Karakterek száma szóközök nélkül:", len(mondat.replace(" ", "")))
