film_cim = input("")
# 'a' karakter keresese
karakter = 'a'

# Szoveg felezese
felezo_index = len(film_cim) // 2

# Karakter indexenek keresese
index = film_cim.find(karakter)

if index != -1:
    # Ha az 'a' karakter megtalalhato
    if index < felezo_index:
        print(f"Az '{karakter}' karakter szerepel, es eloszor az elso feleben szerepelt.")
    else:
        print(f"Az '{karakter}' karakter szerepel, de a masodik feleben szerepelt.")
else:
    # Ha nincs benne az 'a' karakter
    print(f"Sajnos az '{karakter}' karakter nem szerepelt a szovegben.")