szöveg = input("Adja meg a vizsgálni kívánt szöveget: ")

def decode_message(szöveg):
    szavak = szöveg.split()
    titkos = ""

    for i in range(1, len(szavak), 2):
        titkos += szavak[i]

    return titkos

# Kiírás
print("Titkos üzenet:", decode_message(szöveg))
        