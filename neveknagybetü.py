import random

words = ("alma", "narancs", "barack" , "banán" , "kókusz" , "körte")

hangman_art = {0: ("  ",
                   "  ",
                   "  "),
               1: (" O ",
                   "  ",
                   "  "),
               2:( " O ",
                   " | ",
                   "  "),
               3:("  O ",
                   "/| ",
                   "  "),
               4:( " O ",
                   "/|\ ",
                   "  "),
               5:( " O ",
                   "/|\\ ",
                   "/  "),
               6:( " O ",
                   "/|\\ ",
                   "/ \\"),}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_answer(answer)
        guess = input("Adjon meg egy betüt:").lower

if __name__== "__main__":
    main()