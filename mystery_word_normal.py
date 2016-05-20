import random

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
secret_word = random.choice(word_list)
win_tracker = list('_' * len(secret_word)) # maybe use this to track by deleting. multiple letters?
guesses = 8


def welcome():
    print("The computer has picked a secret word. {}: ".format(secret_word))
    print("The word has {} letters.".format(len(secret_word)))


def draw_word():
    for letter in secret_word:
        if letter not in good_guesses:
            print('_ ', end='')
        else:
            print(letter + ' ', end='')


def winner():  # this part definitely not working
    if '_' not in draw_word():
    # del(win_tracker[0])
    # if "_" not in secret_word:
        print("Wow. You did it. Congrats.")


#secret_word_split = list(secret_word)
bad_guesses = []
good_guesses = []
total_guesses = [] # bonus if i can eliminate need for this

welcome()
while guesses > 0:
    print("\n")
    draw_word()
    print("\n")
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
