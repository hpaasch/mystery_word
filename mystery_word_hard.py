import random
import sys

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
secret_word = random.choice(word_list)
guesses = 8


def welcome():
    print("The computer picked a secret word with {} letters.".format(len(secret_word)))
    # print(secret_word)
    # BUILD THIS: let user choose difficulty. Easy 4-6 words. Normal 6-10 words. Hard more than 10 words.



# def user_guess(): BUILD THIS move code from the game loop into function


def draw_word():
    win_tracker = 0
    for letter in secret_word:
        if letter not in good_guesses:
            print('_ ', end='')
            win_tracker += 1
        else:
            print(letter + ' ', end='')
    if win_tracker == 0:
        print("")
        print("Wow. You did it. Congrats.")
        # BUILD THIS add loop that asks user whether they want to restart the game
        sys.exit()


bad_guesses = []
good_guesses = []
total_guesses = []

welcome()
while guesses > 0:
    print("")
    draw_word()
    print("")
    # user_guess()
    while True:
        letter_guess = input("Remaining strikes: {}. Pick a letter: ".format(guesses)).upper()
        if len(letter_guess) == 0:
            print("Nothing was entered.")
        elif not letter_guess.isalpha():
            print("That's not a letter.")
        elif len(letter_guess) > 1:
            print("More than one letter was entered. Pick only one letter at a time.")
        else:
            break
    if letter_guess in total_guesses:
        print("Uh, you already guessed that letter.")
        continue
    if letter_guess in secret_word:
        total_guesses.append(letter_guess)
        good_guesses.append(letter_guess)
        print("Good guess.")
        print("Incorrect guesses: {}.".format(bad_guesses))
    else:
        total_guesses.append(letter_guess)
        bad_guesses.append(letter_guess)
        guesses -= 1
        print("\nAnd that's a miss.")
        print("Incorrect guesses: {}.".format(bad_guesses))
else:
    print("You're out of strikes. You lose. The word was {}.".format(secret_word))

get_words.close()
