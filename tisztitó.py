
text = input(" Adja meg a szöveget: ")

def clean_text(text):
    eredmeny = ""
    elozo = ""  # itt tároljuk az előző karaktert

    for karakter in text:
        if karakter != elozo:
            eredmeny += karakter
        elozo = karakter

    return eredmeny
    
print(clean_text(text))