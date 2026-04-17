while True:
    szam = input(" ")

    # Ellenőrzés: csak szám és megfelelő tartomány
    if szam.isdigit():
        szam = int(szam)
        if 10 <= szam <= 9999:
            # Számjegyek szorzatának kiszámítása
            szorzat = 1
            while szam > 0:
                szorzat *= szam % 10
                szam //= 10

            print(f"A szamjegyek szorzata: {szorzat}")
            break
        else:
            print("A megadott szam nem felel meg a felteteleknek.")
    else:
        print("Hibas bemenet! Kerem, csak szamokat adjon meg.")