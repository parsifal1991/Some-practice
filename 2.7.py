rendszam = input()

# 1. Először hosszellenőrzés:
if len(rendszam) != 7:
    print("Helytelen rendszam hossz.")
else:
    # 2. Ha jó a hossz, nézzük tovább!
    helyes = True
    
    # 3. Első három karakter betű?
    for c in rendszam[0:3]:
        if not c.isalpha():
            print("Az elso harom karakternek betunek kell lennie.")
            helyes = False

    # 4. Negyedik karakter kötőjel?
    if rendszam[3] != '-':
        print("A negyedik karakternek kotojelnek kell lennie.")
        helyes = False

    # 5. Utolsó három karakter szám?
    for c in rendszam[4:7]:
        if not c.isdigit():
            print("Az utolso harom karakternek szamjegyeknek kell lenniuk.")
            helyes = False

    # 6. Ha minden jó, akkor ezt írjuk ki:
    if helyes:
        print("A megadott rendszam helyes formatumu.")