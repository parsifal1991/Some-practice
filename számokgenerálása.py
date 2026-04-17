import random

számok = []
hárommal_osztható_számok = []
páros_számok = []
legkisebb_szám = 100
legnagyobb_szám = 0

while len(számok) < 10:
    szám = random.randint(1,100)
    számok.append(szám)

for szám in számok:
    if szám % 3 ==0:
        hárommal_osztható_számok.append(szám)

for szám in számok:
    if szám % 2 ==0:
        páros_számok.append(szám)

legkisebb_szám = min(számok)
legnagyobb_szám =max(számok)
        
print("Hárommal osztható számok:",len(hárommal_osztható_számok))
print("Számok összege:",sum(számok))
print("Páros számok darabszáma:",len(páros_számok))
print("Legkisebb szám:",legkisebb_szám)
print("Legnagyobb szám:",legnagyobb_szám)

