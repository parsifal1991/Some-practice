import string

mondat = input("")

# Szóközök és írásjelek eltávolítása, kisbetűssé alakítás
mondat_tisztitott = ""
for karakter in mondat:
    if karakter.isalnum():  # csak betűk és számok maradnak
        mondat_tisztitott += karakter.lower()

# Megfordított változat
mondat_forditva = mondat_tisztitott[::-1]

# Ellenőrzés
if mondat_tisztitott == mondat_forditva:
    print("Ez a mondat palindrom.")
else:
    print("Ez a mondat nem palindrom.")