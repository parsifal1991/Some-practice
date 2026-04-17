katona_eletero = int(input())  
tank_sebzes = int(input())  

while katona_eletero > 0:  
    katona_eletero -= tank_sebzes  
    if katona_eletero > 0:  
        print(f"A katona eletereje most: {katona_eletero}")  
    else:  
        print("A katona eletereje most: 0")  # Kiírja a 0-t, mielőtt meghal  
        print("A katona meghalt, a tank nyert!")  
        