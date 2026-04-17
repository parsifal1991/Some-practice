
import random
from collections import Counter

mennyiség = int(input("Adja meg hány darab számot szeretne megvizsgálni: "))

számok = []
while len(számok) < mennyiség:
    szám = random.randint(1, 100)
    számok.append(szám)

# Leggyakoribb szám meghatározása
gyakoriság = Counter(számok)
leggyakoribb_szám = gyakoriság.most_common(1)[0][0]

# Különböző számok listázása
különböző_számok = list(set(számok))

# Páros és páratlan számok különválogatása
páros_számok = [sz for sz in számok if sz % 2 == 0]
páratlan_számok = [sz for sz in számok if sz % 2 != 0]

# Legkisebb páros szám meghatározása (ha van)
if páros_számok:
    legkisebb_páros = min(páros_számok)
else:
    legkisebb_páros = "Nincs páros szám"

# Legtöbbször előforduló páratlan szám meghatározása (ha van)
if páratlan_számok:
    páratlan_gyakoriság = Counter(páratlan_számok)
    legtöbbször_páratlan = páratlan_gyakoriság.most_common(1)[0][0]
else:
    legtöbbször_páratlan = "Nincs páratlan szám"

# Eredmények kiírása
print("Eredeti számok:", számok)
print("Leggyakoribb szám:", leggyakoribb_szám)
print("Különböző számok:", különböző_számok)
print("Legkisebb páros szám:", legkisebb_páros)
print("Legtöbbször előforduló páratlan szám:", legtöbbször_páratlan)