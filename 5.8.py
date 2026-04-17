from math import pi, floor

atmero = int(input("Adja meg a pizza átmérőjét (cm): "))
kozponti_szog = 54
zoli = (kozponti_szog / 360) * pi * (atmero / 2) ** 2
pizza_terulet = pi * (atmero / 2) ** 2

peti = 10 * atmero
peti_szog = floor((peti / pizza_terulet) * 360)

timi_szog_valos = 2 * (180 / pi)
timi = (timi_szog_valos / 360) * pizza_terulet
timi_szog = floor(timi_szog_valos)

dina = pizza_terulet - (zoli + peti + timi)
dina_szog = 360 - (kozponti_szog + peti_szog + timi_szog)

print(f"Atmero: Zoli resze: {floor(zoli)} cm2")
print(f"Kozeponti szog: {kozponti_szog} fok")
print(f"Peti resze: {floor(peti)} cm2")
print(f"Kozeponti szog: {peti_szog} fok")
print(f"Timi resze: {floor(timi)} cm2")
print(f"Kozeponti szog: {timi_szog} fok")
print(f"Dina resze: {floor(dina)} cm2")
print(f"Kozeponti szog: {dina_szog} fok")