
text = str(input("Adja meg a szöveget:"))

def sum_hidden_numbers(text):
    
    számokösszege=0
    
    for karakter in text:
        if karakter.isdigit():
            számokösszege = karakter + számokösszege
            return számokösszege
print(sum_hidden_numbers(text))