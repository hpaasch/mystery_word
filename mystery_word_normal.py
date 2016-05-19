import random

def welcome():
    print("The computer has picked a secret word. {}: ".format(secret_word))
    print("_ " * len(secret_word))

def draw_word():
    for letter in secret_word:
        if letter in good_guesses:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')


get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))

secret_word = random.choice(word_list)

guesses = 8

secret_word_split = list(secret_word)
bad_guesses = []
good_guesses = []
total_guesses = [] # bonus if i can eliminate need for this

welcome()
while guesses > 0:
    draw_word()
    print("\n")
    letter_guess = input("You have {} strikes remaining. Pick a letter: ".format(guesses)).upper()
    if letter_guess in total_guesses:
        print("Uh, you already guessed that letter.")
        continue

    if letter_guess in secret_word:
        total_guesses.append(letter_guess)
        good_guesses.append(letter_guess)
        if good_guesses == secret_word_split:
            print("Wow. You did it. Congrats.")
            break
        #replace the underscore with the letter
        print("Good guess.")
        print("Incorrect guesses so far: {}.".format(bad_guesses))
    else:
        total_guesses.append(letter_guess)
        bad_guesses.append(letter_guess)
        guesses -= 1
        print("And that's a miss.")
        print("Incorrect guesses so far: {}.".format(bad_guesses))
else:
    print("You're out of strikes. You lose. The word was {}.".format(secret_word))

get_words.close()

# DONE import /usr/share/dict/words
# DONE select a random word from it
# DONE count the letters and print that as a number and as blanks
# DONE user input one letter (can assume they only type one letter)
# DONE correct for case -- .upper user input
# DONE is the letter in the random word, and print y/n
# pop letters from secret_word list for each correct guess. then win = list empty
# update the blanks and print .Maybe split the word?
# DONE max 8 guesses.
# DONE tell user how many guesses remain.
# DONE only decrement guesses for a wrong guess.
# DONE if same letter guessed again, print that but don't decrement guesses
# game ends when word guessed or guesses are gone.
# DONE reveal word if guesses gone.
