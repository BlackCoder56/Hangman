import random

words = ["Joan", "Fashion", "Soda", "Minor", "Radio"]

hangman_art = {
    0: (" o "),
    1: (" o ",
        "/"),
    2: (" o ",
        "/|"),
    3: (" o ",
        "/|\\"),
    4: (" o ",
        "/|\\",
        "/"),
    5: (" o ",
        "/|\\",
        "/ \\")
}


def showHint(hint):
    return "".join(hint)

random_word = random.choice(words)
cleaned_word = random_word.lower()

hint = ["_ "]*len(random_word)
is_running = True
guess_count = 0
time_lapse = 5

while is_running:
    guessed_letter = input("Guess Letter: ").lower()
    # print(hint)

    # print(random_word)
    # print(guessed_letter)

    if guessed_letter not in cleaned_word:
        # showArt()
        time_lapse -= 1
        guess_count += 1
        print("Incorrect, Try Again!")
        print("You have ", time_lapse, " times remaining.")
        print(showHint(hint))
        
    for index, letter in enumerate(cleaned_word):
        if letter == guessed_letter:
            hint[index] = guessed_letter
            print(showHint(hint))

    if guess_count == 5:
        print("You lose")
        is_running = False
