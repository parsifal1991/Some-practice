
# Teljes munkaidő és javítási idő percekben
osszes_ido = 480  # 8 óra = 480 perc
javitasi_ido = 45  # Egy autó javítási ideje
megjavitott_autok = 0  # Megjavított autók száma

# Bemenet bekérése
ebedszunet= int(input())  # Ebédszünet hossza
kaveszunet = int(input())  # Kávészünet hossza

# Kezdeti aktív munkaidő (összes időből levonjuk az ebédszünetet)
aktiv_munkaido = osszes_ido - ebedszunet

while aktiv_munkaido >= javitasi_ido:
    megjavitott_autok += 1  # Növeljük a javított autók számát
    aktiv_munkaido -= javitasi_ido  # Levonjuk a javítási időt

    # Minden harmadik autó után kávészünet jön
    if megjavitott_autok % 3 == 0:
        # Csak akkor vonunk le kávészünetet, ha van elég idő rá
        if aktiv_munkaido >= kaveszunet + javitasi_ido:
            aktiv_munkaido -= kaveszunet
        else:
            break  # Ha nincs már elég idő egy újabb autóra, leállunk

print(megjavitott_autok)