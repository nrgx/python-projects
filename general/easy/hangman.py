"""
Notes for refactoring
Avoid globals
Validate inputs
"""

import random
import time

count = 0
display = ""
word = ""
guessed = []
length = 0
play_game = ""


def main():
    global count
    global display
    global word
    global guessed
    global length
    global play_game
    print("The hangman game")
    name = input("Enter your name: ")
    print(f"Hello {name}, we'll starting soon")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    # change with external API call to a word randomizer
    word_candidates = ["january", "beach", "table", "apple", "music"]
    word = random.choice(word_candidates)
    length = len(word)
    count = 0
    display = "_" * length
    guessed = []
    play_game = ""


def loop():
    global play_game
    play_game = input("Do you want to play the game? [Y|N]\n")
    while play_game not in ["Y", "N", "Yes", "No", "y", "n", "yes", "no"]:
        play_game = input("Do you want to play the game? [Y|N]\n")
    if play_game in ["Y", "Yes", "y", "yes"]:
        main()
    else:
        print("GG WP")
        exit()


def hangman():
    global count
    global display
    global word
    global guessed
    global play_game
    limit = 5
    guess: str = input(f"{display}\n")
    guess = guess.strip()
    if len(guess) == 0 or len(guess.split()) > 1 or guess.isdigit():
        print("Invalid input. Try again.")
    elif guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1 :]
        display = display[:index] + guess + display[index + 1 :]
        print(f"{display}\n")
    elif guess in guessed:
        print("Try another letter")
    else:
        count += 1
        warning = f"Wrong guess. {limit - count} guesses left.\n"
        if count == 1:
            time.sleep(1)
            print(
                "   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print(warning)
        elif count == 2:
            time.sleep(1)
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print(warning)
        elif count == 3:
            time.sleep(1)
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print(warning)
        elif count == 4:
            time.sleep(1)
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |     0\n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print(warning)
        elif count == 5:
            time.sleep(1)
            print(
                "   _____   \n"
                "  |     |  \n"
                "  |     |  \n"
                "  |     |  \n"
                "  |     0  \n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "__|__\n"
            )
            print(f"You are hanged. The word was {guessed}, {word}")
            loop()
    if word == "_" * length:
        print("Congratulations! You guesses the word")
        loop()
    elif count == limit:
        hangman()
    hangman()


if __name__ == "__main__":
    loop()
    print(f"You need to guess the word {display}")
    hangman()
