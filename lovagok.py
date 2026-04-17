
lovagok = input("Adja meg a lovagokat:")

def balance_check(lovagok):
    jók = 0
    gonoszak = 0
    for karakter in lovagok:
        if karakter == 'G' or 'g':
            gonoszak += 1
        elif karakter == 'J' or 'j':
            jók += 1
        if gonoszak > jók:
            return True
        
    return False
    
print(balance_check(lovagok))