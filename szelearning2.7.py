rendszam = input()

if len(rendszam) != 7:
    print("Helytelen rendszam hossz.")
elif not rendszam[0].isalpha() or not rendszam[1].isalpha() or not rendszam[2].isalpha():
    print("Az elso harom karakternek betunek kell lennie.")
elif rendszam[3] != "-":
    print("A negyedik karakternek kotojelnek kell lennie.")
elif not rendszam[4].isdigit() or not rendszam[5].isdigit() or not rendszam[6].isdigit():
    print("Az utolso harom karakternek szamjegyeknek kell lenniuk.")
else:
    print("A megadott rendszam helyes formatumu.")
