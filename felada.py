gyumolcsok = []

while len(gyumolcsok) < 5:
    gyumolcs = input(" Adja meg gyümölcsöt: ")
    if gyumolcs in gyumolcsok:
        print(" Ez mar volt!")
    elif "e" in gyumolcs:
        print(" A gyumolcs neveben 'e' betu van!")
    else:
        gyumolcsok.append(gyumolcs)
        
tuple_gyumolcsok = [(index + 1, gyumolcs) for index, gyumolcs in enumerate(gyumolcsok)]

for index, gyumolcs in enumerate(gyumolcsok, start=1):
    print(f"{index}. {gyumolcs}")