import random

words = ["Joan", "Fashion", "Soda", "Minor", "Radio"]

hangman_art = {
    0: (" o "),
    1: (" o ",
        " | "),
    2: (" o ",
        " | "
        "/"),
    3: (" o ",
        " | ",
        "/ \\"),
    4: (" o ",
        " | ",
        "/ \\",
        " | "),
    5: (" o ",
        " | ",
        "/ \\",
        " | ",
        "/"),
    6: (" o ",
        "/|\\",
        "/ \\"),
    
}

for line in hangman_art[6]:
    print(line)


# def showHint(hint):
#     return "".join(hint)

# random_word = random.choice(words)

# hint = ["_ "]*len(random_word)
# is_running = True
# guess_count = 0

# while is_running:
#     guessed_letter = input("Guess Letter: ").lower()
#     # print(hint)

#     print(random_word)
#     print(guessed_letter)

#     if guessed_letter not in random_word:
#         # showArt()
#         guess_count += 1
        
#     for index, letter in enumerate(random_word):
#         if letter == guessed_letter:
#             hint[index] = guessed_letter
#             print(showHint(hint))

#     if guess_count == 6:
#         print("Ended")
#         break
