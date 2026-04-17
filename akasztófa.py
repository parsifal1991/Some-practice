import random

words = (
    "kutya", "macska", "elefánt", "kakadu", "ember", "lada", "bicikli",
    "bölömbika", "szennyeskosár", "csincsilla", "transformers", "gandalf",
    "harrypotter", "lapátnyél", "marharépa"
)

hangman_art = {
    0: ("     ", "     ", "     "),
    1: (" O   ", "     ", "     "),
    2: (" O   ", " |   ", "     "),
    3: (" O   ", "/|   ", "     "),
    4: (" O   ", "/|\\  ", "     "),
    5: (" O   ", "/|\\  ", "/    "),
    6: (" O   ", "/|\\  ", "/ \\ "),
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("A megoldás:", " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print("\n🕹️ Akasztófa játék kezdődik! Tippelj egyesével betűket.\n")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print("Már tippelt betűk:", ", ".join(sorted(guessed_letters)))
        guess = input("Adjon meg egy betűt: ").lower()  # ✅ Helyes inputkezelés!

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Csak egyetlen betűt adjon meg!\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️ A(z) '{guess}' betűt már tippelte.\n")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ A(z) '{guess}' nincs a szóban.\n")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("\n🎉 Gratulálok, nyertél!")
            print("A szó:", answer)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("\n💀 Vesztettél!")
            display_answer(answer)
            is_running = False

if __name__ == "__main__":
    main()