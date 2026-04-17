szemelyi = input()

if len(szemelyi) != 11:
    print("A megadott azonosito nem 11 szamjegybol all.")
else:
    osszeg = 0
    for i in range(10):
        osszeg += int(szemelyi[i]) * (i + 1)

    maradek = osszeg % 11

    if maradek == int(szemelyi[10]):
        print("A szemelyi azonosito valodi.")
    else:
        print("A szemelyi azonosito nem valodi.")