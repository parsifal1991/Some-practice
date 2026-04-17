
számok = []
páros = []
páratlan = []


while len(számok) < 10 :
    szám = int(input("Adja meg a számokat amivel dolgozni szeretne:"))
    számok.append(szám)
    
for szám in számok:
    if szám % 2 == 0:
        páros.append(szám)
    else:
        páratlan.append(szám)

páros_összege = sum(páros)
páratlan_összege = sum(páratlan)

if páros_összege == páratlan_összege:
    print("A páros és páratlan számok összege egyenlő.")
else:
    print("A páros és páratlan számok különbsége:",páratlan_összege - páros_összege)
