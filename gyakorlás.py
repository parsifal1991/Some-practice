
n = int(input("Adjon meg egy pozitív egész számot: "))


def even_odd_digit_check(n):
    páros = n % 2 == 0
    páratlan = n % 2 != 0
    for számjegy in str(n):
        if int(számjegy) % 2 == 0:
            páros += 1
        elif int(számjegy) % 2 != 0:
            páratlan += 1
        return páros == páratlan
    
print(even_odd_digit_check(1234))
print(even_odd_digit_check(1223))