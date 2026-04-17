import random

is_running = True
guesses = 0
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

print(" Welcome to the number guessing game! ")
print(f" Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")  # Szövegként olvasd be!
    if guess.isdigit():
        guess = int(guess)  # Csak ekkor alakítsd számmá
        guesses += 1  # Növeld a számlálót

        if guess < lowest_num or guess > highest_num:
            print("The given number is out of range!!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("The number is too low")
        elif guess > answer:
            print("The number is too high")
        else:
            print(f"You have found the number! Good job!{answer}")
            print(f"Number of guesses:{guesses}")
            is_running = False
    else:
        print("Invalid input! Please enter a number.") 

        