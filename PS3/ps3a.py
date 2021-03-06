"""
Template for word game.

# Josh Haines
# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>

"""
import random
from sys import exit
# import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Return a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r', 1)
    # wordlist: list of strings
    wordlist = []
    for line in in_file:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Go get a dictionary.

    Return a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word


def get_word_score(word, n):
    """
    Return the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters
    in the word multiplied by the length of the word, plus 50
    points if all n letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    n: int, number of letters required for a bonus score
    returns: int >= 0
    """
    score = 0  # init score to zero on each call
    for letter in list(word):
        score = score + SCRABBLE_LETTER_VALUES[letter]
    score = score * len(word)
    if len(word) == n:
        score = score + 50
    return score

get_word_score("alphabet", 7)
#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    """
    Display the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    display = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            display.append(letter)
            # print(letter,)             # print all on the same line
    display = ' '.join(display)          # print an empty line
    return display

#
# Make sure you understand how this function works and what it does!
#


def deal_hand(n):
    """
    Return a random hand containing n lowercase letters.

    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = round(n / 3)

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Assume that 'hand' has all the letters in word.

    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # Get the old hand into a list.
    interim_hand = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            interim_hand.append(letter)

    # Remove letters of word from interim_hand
    for i in list(word):
        interim_hand.remove(i)

    # return the new hand
    return(get_frequency_dict(interim_hand))
#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Check if a word is valid.

    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    word_dict = get_frequency_dict(word)
    try:
        for key in word_dict.keys():
            if word_dict[key] > hand[key]:
                # print('More {}s in word than in hand.'.format(key))
                return False
            # else:
                # print('Less or equal {}s in word than in hand.'.format(key))
    except KeyError:
            return False

    if ''.join(list(word)) in word_list:
        return True
    else:
        return False


def calculate_handlen(hand):
    """Calculate the handlength."""
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#


def play_hand(hand, word_list):
    """
    Actually play the hand.

    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings

    """
    end_hand = 0
    hand_total = 0
    while calculate_handlen(hand) > 0 and end_hand == 0:
        print()
        print('Your Hand: {}'.format(display_hand(hand)))
        print()

        # loop until given a valid word
        valid_word = 0
        word_total = 0
        while valid_word == 0:
            print('Enter a valid word, or a "." to indicate you are finished.')
            word = input('>>>')
            if word == '.':
                print('Total Score: {}'.format(hand_total))
                return hand_total
            elif is_valid_word(word, hand, word_list) is False:
                print('That word is invalid.')
                valid_word = 0
            else:
                word_total = get_word_score(word, calculate_handlen(hand))
                hand_total += word_total
                print('"{}"" earned {} points.  Hand total: {} points.'.format(
                      word, word_total, hand_total))
                valid_word = 1

        hand = update_hand(hand, word)

    # Return

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#


def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    old_hand = deal_hand(HAND_SIZE)  # Make sure old hand isn't empty

    # Opening Message
    score = 0
    play = 1
    while play == 1:
        new_hand = deal_hand(HAND_SIZE)
        print('Welcome to the word game.')
        print('Your score is: {}'.format(score))
        print('If you would like to play a new (random) hand, press "n".')
        print('If you would like to play the last hand again, press "r".')
        print('If you would like to exit, press "e"')
        choice = input('>>> ')

        if choice == 'n':
            score += play_hand(new_hand, word_list)
            old_hand = new_hand  # Update the old hand with the new one
        elif choice == 'r':
            score += play_hand(old_hand, word_list)
        elif choice == 'e':
            play = 0
        else:
            print('Your selection was not understood.  Try again... ')

    print('Thanks for playing!')
    exit()
#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
