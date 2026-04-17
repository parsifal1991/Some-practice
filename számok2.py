
import random

számok = []
páros = []
páratlan = []

while len(számok) < 10:
    szám = random.randint(1,100)
    számok.append(szám)
    
for szám in számok:
    if szám % 2 == 0:
        páros.append(szám)
    else:
        páratlan.append(szám)
        
páros_átlag = sum(páros) / len(páros)
páratlan_átlag = sum(páratlan) / len(páratlan)

if páros_átlag > páratlan_átlag:
    print("A páros számok átlaga a nagyobb:",páros_átlag)
elif páratlan_átlag > páros_átlag:
    print("A páratlan számok átlaga a nagyobb:",páratlan_átlag)
else:
    print("A két átlag egyenlő!")