csoki=600                         #csoki ára
gumicukor=400                     #gumicukor ára
keksz=550                         #keksz ára
doboz_sutemeny=1200               #doboz sütemény ára
penz=10000
hitel=0
megmaradt=0

csoki_db=int(input("Hany csokit vasarol?"))
gumicukor_db=int(input(" Hany gumicukrot vasarol?"))
keksz_db=int(input(" Hany kekszet vasarol?"))
doboz_sutemeny_db=int(input(" Hany doboz sutemenyt vasarol?"))
borravalo=int(input(" Mennyi borravalot ad?"))

osszes_koltseg=(csoki_db*csoki)+(gumicukor_db*gumicukor)+(keksz_db*keksz)+(doboz_sutemeny_db*doboz_sutemeny)+(borravalo)

if osszes_koltseg>penz:
    hitel=osszes_koltseg-penz
    print(f" Hitelre vasarolt: {hitel} Ft ertekben")
else:
    osszes_koltseg<=penz
    megmarad=penz-osszes_koltseg
    print(f" Megmarad: {megmarad} Ft")