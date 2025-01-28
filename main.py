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

def showArt(guess_count):
    print("\n***************")
    for line in hangman_art[guess_count]:
        print(line)    
    print("***************")

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
    
    if guessed_letter == "":
        print("Please enter a Letter!")
        continue

    if guessed_letter not in cleaned_word:
        showArt(guess_count)
        if time_lapse != 0:
            print("Incorrect guess, Try Again!")
            print("You have ", time_lapse, " times remaining.")
            print(showHint(hint))
        else:
            print("You're out of Guesses!")
        
        time_lapse -= 1
        guess_count += 1      
        
    for index, letter in enumerate(cleaned_word):
        if letter == guessed_letter:
            hint[index] = guessed_letter
            print(showHint(hint))
    
    x = "".join(hint)
    if x == cleaned_word:
        print("\nYou Win")
        is_running = False

    if guess_count == 6:
        print("You LOSE")
        is_running = False
