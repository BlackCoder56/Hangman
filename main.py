import random as ran
from words import words

words = words


# Method to print hangman Art
def shoArt(trials):
    # Hangman dictionary of tuples
    art = {
        0:(" o "),
        1:("       o ",
           "      /"),
        2:("       o ",
           "      /|"),
        3:("       o ",
           "      /|\\"),
        4:("       o ",
           "      /|\\",
           "      /"),
        5:("       o ",
           "      /|\\",
           "      / \\")
    }
    # for loop to print art line by line
    for line in art[trials]:
        print(line)

# Function to return random word hint without spaces
def showHint(hint):
    return "".join(hint)

# Main function to do most of the work
def main():
    # trials variable to keep track of the number of incorrect guesses
    trials = 0

    # is_running boolean is True when trials are not 6
    # Or the random word has not been guessed yet.
    is_running = True

    # ranword stores a random word from a List
    ranword = ran.choice(words)

    # hint replaces letters in the random word with underscores
    # eg. ["_ ", "_ ", "_ "]
    hint = ["_ "]*len(ranword.lower())

    print("Welcome to my hangman app:")

    # iniputt variable stores abstract value before user's input
    iniputt = ''

    # The loop runs basing on it's conditions
    while(iniputt != 'q' and iniputt != 'Q'):
        # This is a prompt and stores user input in iniputt
        iniputt = input("If you want to start a new game:\n1. Press enter. \n2. To quit game press quit(q/Q): ")

        # if statement to check user input
        if iniputt.lower() == 'q':
            print("###############")
            print("## GoodBye!! ##")
            print("##############")
            continue
        # if statement to check user input
        elif iniputt == "":
            while(is_running):
                # prints hint
                print(showHint(hint))

                # Prompts user to input a single letter
                user_input = input("Enter your letter: ")

                # Checking if user input value is in random word
                if user_input.lower() in ranword.lower():
                    # Looping through the random word
                    for index, letter in enumerate(ranword.lower()):
                        # if statement checks letters index in random word
                        if letter.lower() == user_input.lower():
                            hint[index] = letter.lower()
                            # print(showHint(hint))
                else:
                    if trials == 5:
                        print("\n")
                        print("*****************")
                        shoArt(trials)
                    else:
                        print(showHint(hint))
                        shoArt(trials)                    
                    trials += 1

                cleaned = showHint(hint)

                if cleaned.capitalize() == ranword.capitalize():
                    print("\n")
                    print("*******************")
                    print("You Won!")
                    print(f"The word was \"{ranword.capitalize()}\"")
                    print("*****************")
                    print("\n")
                    is_running = False
                elif trials == 6:
                    print("You LOST!")
                    print(f"The word was \"{ranword.capitalize()}\"")
                    print("Try Again Later.")
                    print("*******************")
                    print("\n")
                    is_running = False

            # Reseting Assests
            is_running = True
            trials = 0
            is_running = True
            ranword = ran.choice(words)
            hint = ["_ "]*len(ranword.lower())
        else:
            print("################")
            print("#Invalid Input!#")
            print("################")

main()
