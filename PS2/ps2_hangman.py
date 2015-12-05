"""Code the game hangman.

#  6.00 Problem Set 3
#  Name: Josh Haines
#  Collaborators: None
#  Time Spent: ~7hrs
#  Hangman

#  -----------------------------------
#  Helper code
#  (you don't need to understand this helper code)
"""

import random
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """Return a list of valid words.

    Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    #  in_file: file
    in_file = open(WORDLIST_FILENAME, mode="r", buffering=-1)
    #  line: string
    line = in_file.readline()
    #  word_list: list of strings
    word_list = str.split(line)
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    """word_list (list): list of words (strings).

    Returns a word from word_list at random
    """
    return random.choice(word_list)

#  end of helper code
#  -----------------------------------


def update_blank_list(list, position, letter):
    """Take in the blank list and update it.

    Update the list by adding any of the new letters to it which were correct.

    Update the location in "list" indicated by "position" with the "letter".
    Send back the list when finished.
    """
    list[position] = letter
    return list


def play():
    """Start function starts the game.

    No Inputs, no outputs except printing.
    We'll allow the player to "play again" or quit."

    First we will load in a list of words and choose one of them.

    Then we'll use a function (update_blank_list) which will update and return
    a correct blank list for our game (something like _ _ e _ _).

    We'll start off a loop that cycles down the number of guesses if wrong,
    and doesn't if right.
    """
    # variable
    num_guesses_left = 8  # number of guesses per game
    alphabet_left = "abcdefghijklmnopqrstuvwxyz"  # starting alphabet
    # blank_list = bytearray(str)  #  _ _ e _ _ variable

    #  Get a word
    #  actually load the dictionary of words and point to it with
    #  the word_list variable so that it can be accessed from anywhere
    #  in the program
    # word_list = load_words()
    word_list = load_words()
    word = choose_word(word_list)
    word = list(word)
    blank_list = list(word)

    # generate blank_list
    for i in range(len(word)):
        blank_list[i] = "_"

    #  Opening game text
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d letters long." % len(word))

    #  Start Game
    while num_guesses_left > 0:
        wrong_guess = 0
        print("--------------------")
        print("You have %d guesses left." % num_guesses_left)
        print("Available Letters: %s" % alphabet_left)
        letter_guess = input("Please guess a letter: ")
        alphabet_left = alphabet_left.replace(letter_guess, "")
        for ii in range(len(word)):
            if word[ii] == letter_guess:
                blank_list = update_blank_list(blank_list, ii, letter_guess)
            else:
                wrong_guess += 1
        if wrong_guess < len(word):
            print("Good Job: %s" % " ".join(blank_list))
        else:
            print("Oops! That letter is not in my word: %s" % " ".
                  join(blank_list))
            num_guesses_left += -1
        if "_" not in blank_list:
            return "won"
    if "_" in blank_list:
        print("The word was %s." % " ".join(word))
        return "lost"
    else:
        return "won"


def start():
    """Cycle the game over and over until player is done."""
    play_again = "y"

    while play_again == "y":
        outcome = play()
        if outcome == "lost":
            print("Game Over, You Lost.")
        elif outcome == "won":
            print("Congratulations, You Won!")
        else:
            sys.exit("Houston, we have a problem...")
        play_again = input("Do you want to play again? y or n ")
    sys.exit("Thanks for playing!")

start()
#  end
