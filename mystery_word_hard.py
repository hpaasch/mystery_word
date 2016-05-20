import random
import sys

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
word_list_easy = []
word_list_normal = []
word_list_hard = []
for word in word_list:
    if len(word) == 4:
        word_list_easy.append(word)
    if len(word) == 6:
        word_list_normal.append(word)
    if len(word) > 9:
        word_list_hard.append(word)

# secret_word = random.choice(word_list)
secret_word = ()
guesses = 8


def game_start():
    global secret_word
    game_level = int(input("Enter 1 for Easy, 2 for Normal or 3 for Hard version of the game. "))
    if game_level == 1:
        secret_word = random.choice(word_list_easy)
    if game_level == 2:
        secret_word = random.choice(word_list_normal)
    if game_level == 3:
        secret_word = random.choice(word_list_hard)
    return secret_word
    #print("The computer picked a secret word with {} letters.".format(len(secret_word)))
    # print(secret_word)
    # Easy 4-6 words. Normal 6-10 words. Hard more than 10 words.



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

game_start()
print("The computer picked a secret word with {} letters.".format(len(secret_word)))
print(secret_word)
while guesses > 0:
    print("")
    draw_word()
    print("")
    # user_guess starts here
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
    # user_guess to here
else:
    print("You're out of strikes. You lose. The word was {}.".format(secret_word))

get_words.close()
