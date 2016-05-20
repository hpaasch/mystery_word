import random
import sys

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
secret_word = random.choice(word_list)
guesses = 8


def welcome():
    print("The computer picked a secret word with {} letters.".format(len(secret_word)))
    # print(secret_word)


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
        sys.exit()


bad_guesses = []
good_guesses = []
total_guesses = []

welcome()
while guesses > 0:
    print("")
    draw_word()
    print("")
    letter_guess = input("Remaining strikes: {}. Pick a letter: ".format(guesses)).upper()
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
