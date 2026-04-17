phone_number = input("Enter your phonen umber:")
# result = len(name) hosszuságát adja meg a sztringnek!
# result = name.find("B") keresni tudunk a sztringben és az első keredsendő karakter pozicióját adja meg ballrol jobbra
# result = name.rfind("B") keres a sztringben hátulról kezdve, jobbrol ballra adja meg az első keresett karaktert
# name = name.capitalize() csak az első szó kezdőbetűjét változtatja nagy betűre
# name = name.upper() minden karaktert nagybetűre változtat
# name = name.lower() minden karaktert kisbetűre változtat
# result = name.isdigit() csak akkor ir ki true választ ha minden karakter szám
# result = name.isalpha() csak akkor igaz ha betűk vannak csak a sztrinben, szoköz sem lehet!
# result = phone_number.count("-") meg lehet számoltatni vele hány adott karakter van a sztringben
phone_number =phone_number.replace("-"," ")

print (phone_number)