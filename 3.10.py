import math

eger_poz = 25
macska_poz = 10

eger_seb = int(input())
macska_seb = int(input())

if macska_seb <= eger_seb:
    print("Sosem kapja el")
else:
    tav = eger_poz - macska_poz
    ido = tav / (macska_seb - eger_seb)
    elkapasi_pont = eger_poz + eger_seb * ido
    print(math.ceil(elkapasi_pont))