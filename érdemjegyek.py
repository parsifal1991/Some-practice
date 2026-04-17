
jegyek = []
elégtelen = []
elégséges = []
közepes = []
jó = []
jeles = []

jegy = int(input( " Adja meg az érdemjegyeket: "))
if jegy > 5 or jegy < 1 :
    print( " A megadott érték nem megfelelő, adjon meg egy másikat: ")
else:
    jegyek.append(jegy)

while len(jegyek) < 10:
    jegy = int(input( " Adja meg az érdemjegyeket: "))
    if jegy > 5 or jegy < 1 :
        print( " A megadott érték nem megfelelő, adjon meg egy másikat: ")
    else:
        jegyek.append(jegy)

for jegy in jegyek:
    if jegy == 1:
        elégtelen.append(jegy)
    elif jegy ==2:
        elégséges.append(jegy)
    elif jegy == 3:
        közepes.append(jegy)
    elif jegy == 4:
        jó.append(jegy)
    elif jegy == 5:
        jeles.append(jegy)

jegyek_átlaga = sum(jegyek) / len(jegyek)

print("Jegyek átlaga:",round(jegyek_átlaga,2))
print("Elégtelen osztályzatok száma:",len(elégtelen),"🤧")
print("Elégséges osztályzatok száma:",len(elégséges),"☹️")
print("Közepes osztályzatok száma:",len(közepes),"🫤")
print("Jó oszályzatok száma:",len(jó),"🙂")
print("Jeles osztályzatok száma:",len(jeles),"😊")