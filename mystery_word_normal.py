# DONE import /usr/share/dict/words
# DONE select a random word from it
# DONE count the letters and print that as a number and as blanks
# DONE user input one letter (can assume they only type one letter)
# DONE correct for case -- .upper user input
# DONE is the letter in the random word, and print y/n
# update the blanks and print .Maybe split the word?
# max 8 guesses.
# tell user how many guesses remain.
# only decrement guesses for a wrong guess.
# if same letter guessed again, print that but don't decrement guesses
# game ends when word guessed or guesses are gone.
# reveal word if guesses gone.

import random

get_words = open("/usr/share/dict/words")
word_list = list(get_words.read().upper().split("\n"))
#print(word_list)

secret_word = random.choice(word_list)
#print(secret_word)

#print("Welcome to my Hangman game. The computer picks a word and you get 8 misses to solve it.")
print("Here is the computer's word {}: ".format(secret_word))
print("_ " * len(secret_word))

guesses = 8

letter_guess = (input("You have {} guesses remaining. Pick a letter: ".format(guesses))).upper()
#print(letter_guess)

secret_word_split = secret_word.split()
bad_guesses = []
good_guesses = []

if letter_guess in bad_guesses or good_guesses:
    print("Uh, you already guessed that letter. Try another.")

while guesses > 0:
    if good_guesses == secret_word_split:
        print("Wow. You did it. Congrats.")
        break
    elif letter_guess in secret_word:
        good_guesses.append(letter_guess)
        print("Good guess. You still have {} misses remaining.".format(guesses))
        print("Incorrect guesses so far: {}.".format(bad_guesses))
        break
    else:
        bad_guesses.append(letter_guess)
        guesses -= 1
        print("And that's a miss. You have {} strikes remaining.".format(guesses))
        print("Incorrect guesses so far: {}.".format(bad_guesses))
        break

get_words.close()
