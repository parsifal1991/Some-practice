játékos = input("Add meg a játékos nevét: ")

print(f"{játékos}, üdvözöllek a kalandban!")

# Első döntés: közlekedési mód
while True:
    válasz = input("Küldetésed, hogy eljuttass egy levelet a királynak, minden áron! Utadat lóháton kezded vagy gyalogosan vágnál bele? lóháton/gyalogosan: ").lower()
    if válasz in ["lóháton", "lovon", "ló"]:
        print("Bemész a farmodon lévő istállóba és felnyergeled a lovadat. A király 3 napnyi lovaglásra van, ha csak sötétedéskor állsz meg pihenni.")
        print("Amint összekészültél és a lovad is készen áll az indulásra, már pattannál is a nyeregbe, amikor furcsa zajt hallasz a házad felől.")
        break
    elif válasz in ["gyalogosan", "gyalog"]:
        print("Gyalogosan 12 napba telne eljutni a várig, biztos vagy benne, hogy gyalog vágnál bele? igen/nem")
        válasz = input().lower()
        if válasz == "igen":
            print("Már az első napodon, éjszaka rád támadtak és mire észbe kaptál volna már az üzenetet elvették tőled, téged pedig egy fához kötöztek!")
            print("Vesztettél a játéknak vége!")
            exit()
        elif válasz == "nem":
            print("Bemész a farmodon lévő istállóba és felnyergeled a lovadat. A király 3 napnyi lovaglásra van ha csak sötétedéskor állsz meg pihenni.")
            print("Amint összekészültél és a lovad is készen áll az indulásra, már pattannál is a nyeregbe amikor furcsa zajt hallasz a házad felől.")
            break
        else:
            print("Helytelen válasz! Kérlek válaszolj igennel vagy nemmel.")
    else:
        print("Helytelen válasz! Kérlek válassz: lóháton / gyalogosan.")

# Második döntés: megnézed a zaj forrását vagy indulsz
while True:
    válasz = input("Odamész és megnézed, vagy nem foglalkozol vele, hiszen sietned kell? Megnézem/Indulok: ").lower()
    if válasz == "megnézem":
        print("Mivel nem akarod úgy elhagyni az otthonodat, hogy nem tudod mi volt az a zaj, visszasétálsz és megnézed mi okozta.")
        print("Amint belépsz az ajtón három számodra ismeretlen nagydarab erős katona jelenik meg előtted.")
        print("Esélyed sincs reagálni sem, mire észhez térsz már nyomuk sincs és az üzeneted is hűlt helye van.")
        print("A játéknak vége, vesztettél!")
        break
    elif válasz == "indulok":
        print("Felpattánsz a nyeregbe és már vágtatsz is! Mivel korán reggel van, de már azért jön fel a nap hátra nézel a házadra,")
        print("ahol látod, hogy valakik éppen feldúlják az otthonodat! Nagy kő esik le a szívedről és örülsz, hogy nem nézted meg a zaj forrását!")
        break
    else:
        print("Helytelen választ adtál meg! Kérlek válassz: megnézem / indulok.")