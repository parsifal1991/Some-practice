mondat = input("Adja meg a mondatot: ")

def capitalize_sentence(mondat):
    szavak = mondat.split()
    nagybetűs_szavak = [s.capitalize() for s in szavak]
    megoldás = " ".join(nagybetűs_szavak)
    return megoldás

print(capitalize_sentence(mondat))