import random
import sys
import os

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
word_list_easy = []
word_list_normal = []
word_list_hard = []
for word in word_list:
    if len(word) == 4 or len(word) == 5 or len(word) == 6:  # can this be done another way? 4-6
        word_list_easy.append(word)
    if len(word) == 7 or len(word) == 8 or len(word) == 9:
        word_list_normal.append(word)
    if len(word) > 9:
        word_list_hard.append(word)

# these are global variables
secret_word = ()
good_guesses = []


def game_start():
    global secret_word
    game_level = ()
    print("You're about to play the Magical Mystery Word game. Good luck!")
    while True:
        game_level = (input("Enter 1 for Easy, 2 for Normal or 3 for Hard version of the game. "))
        if game_level == "":
            print("Magical Mystery Word thinks you didn't type a 1, 2, or 3. Type carefully.")
        elif game_level not in ['1', '2', '3']:
            print("Magical Mystery Word thinks you didn't type a 1, 2, or 3. Type carefully.")
        else:
            break
    if game_level == '1':
        secret_word = random.choice(word_list_easy)

    if game_level == '2':
        secret_word = random.choice(word_list_normal)

    if game_level == '3':
        secret_word = random.choice(word_list_hard)
    # os.system('cls' if os.name == 'nt' else 'clear') # only works in Terminal, not in IDE
    return secret_word


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
        replay()


def replay():
    play_again = input("Want to play again? Y/n ").lower()
    if play_again != 'n':
        print("Glad you're up for another go at Magical Mystery Word.")
        print("_" * 40, "\n")
        play()
    else:
        print("Sorry to see you go. Have a nice day!")
        sys.exit()


def play():
    bad_guesses = []
    global good_guesses
    good_guesses = []
    total_guesses = []

    game_start()
    print("\nMagical Mystery Word picked a word with {} letters. Try to figure it out.".format(len(secret_word)))
    # print(secret_word)
    guesses = 8
    while guesses > 0:
        # print("")
        draw_word()
        print("")
        while True:
            letter_guess = input("Remaining misses: {}. Pick a letter: ".format(guesses)).upper()
            if len(letter_guess) == 0:
                print("Nothing was entered.")
            elif not letter_guess.isalpha():
                print("That's not a letter.")
            elif len(letter_guess) > 1:
                print("More than one letter was entered. Pick only one letter at a time.")
            else:
                break
        if letter_guess in total_guesses:
            print("Hmmm. Getting tired? You already guessed that letter.")
            print("\nIncorrect guesses: {}.".format(bad_guesses))
            continue
        if letter_guess in secret_word:
            total_guesses.append(letter_guess)
            good_guesses.append(letter_guess)
            print("Yay! You got one right. Keep going.")
            print("\nIncorrect guesses: {}.".format(bad_guesses))
        else:
            total_guesses.append(letter_guess)
            bad_guesses.append(letter_guess)
            guesses -= 1
            print("And that's a miss.")
            print("\nIncorrect guesses: {}.".format(bad_guesses))
    else:
        print("You're out of strikes. You lose. The word was {}.".format(secret_word))
        replay()

play()

get_words.close()
