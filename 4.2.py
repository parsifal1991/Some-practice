gyumolcsok = []

while len(gyumolcsok) < 5:
    gyumolcs = input("")

    if "e" in gyumolcs:
        print("A gyumolcs neveben 'e' betu van!")
        continue  

    if gyumolcs in gyumolcsok:
        print("Ez mar volt!")
        continue

    gyumolcsok.append(gyumolcs)

gyumolcsoktuple = tuple(gyumolcsok)
print(gyumolcsoktuple)