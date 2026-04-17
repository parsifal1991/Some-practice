szoveg = input()

fele = len(szoveg) // 2
elso = szoveg[:fele]
masodik = szoveg[fele:]

if "a" in szoveg:
    if "a" in elso:
        print("Az 'a' karakter szerepel, es eloszor az elso feleben szerepelt.")
    else:
        print("Az 'a' karakter szerepel, de a masodik feleben szerepelt.")
else:
    print("Sajnos az 'a' karakter nem szerepelt a szovegben.")