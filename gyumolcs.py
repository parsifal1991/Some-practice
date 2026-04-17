gyumolcsok = []

while len(gyumolcsok) < 5:
    gyumolcs = input("Adj meg egy gyümölcsöt: ")

    if 'e' in gyumolcs:
        print("A gyümölcs nevében 'e' betű van! Adj meg egy másikat.")
        continue  # Újra kérjük a bemenetet

    if gyumolcs in gyumolcsok:
        print("Ez a gyümölcs már volt! Adj meg egy másikat.")
        continue  # Újra kérjük a bemenetet

    gyumolcsok.append(gyumolcs)

# Lista tuple-be másolása
gyumolcs_tuple = tuple(enumerate(gyumolcsok, start=1))

# Kiírás
for index, gyumolcs in gyumolcs_tuple:
    print(f"{index}. {gyumolcs}")  # Itt volt a hiba