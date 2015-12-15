from ps3a import *
# import time
from perm import *

#
# Problem #6A: Computer chooses a word
#


def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_dict, find the word that gives the maximum value
    score,    and return it.  This word should be calculated by considering
    all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    from random import randint
    n = 10
    while n > 8:
        n = randint(0, calculate_handlen(hand))

    perms = get_perms(hand, n)
    for i in perms:
        if i in word_list:
            return i
            # Rarely this returns None, make sure to check and
            # re-call this function in case that happens.  It u
            # usually only happens when the random number is very small.
            # The timing also gets out of hand when the random
            # number goes much over 8.  The upper while loop should
            # minimize these problems.
            # Turns out they want None to be the symbol that the computer
            # is done playing...


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices
     (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
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
            word = comp_choose_word(hand, word_list)
            if word == '.':
                print('Total Score: {}'.format(hand_total))
                return hand_total
            elif word is None:
                print('No more plays, hand is over.')
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

#
# Problem #6C: Playing a game
#


def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using
    play_hand.

    * If the user inputs 'c', let the computer play the game using
    comp_play_hand (created above).

    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    old_hand = deal_hand(HAND_SIZE)  # Make sure old hand isn't empty

    # Opening Message
    human_score = 0
    pc_score = 0
    play = 1
    while play == 1:
        new_hand = deal_hand(HAND_SIZE)
        print('Welcome to the word game.')
        print('Human score is: {}'.format(human_score))
        print('PC Score is: {}'.format(pc_score))
        print('If you would like to play a new (random) hand, press "n".')
        print('If you would like to play the last hand again, press "r".')
        print('If you would like to exit, press "e"')
        choice = input('>>> ')
        if choice == 'e':
            print('Thanks for playing!')
            exit()

        print('If you would like to play the next hand, press "u".')
        print('If you would like the computer to play the hand, press "c".')
        print('If you would like to exit, press "e"')
        who_plays = input('>>> ')

        if who_plays == 'u':  # User plays
            if choice == 'n':
                human_score += play_hand(new_hand, word_list)
                old_hand = new_hand  # Update the old hand with the new one
            elif choice == 'r':
                human_score += play_hand(old_hand, word_list)
            else:
                print('Your selection was not understood.  Try again... ')

        elif who_plays == 'c':  # Computer Plays
            if choice == 'n':
                pc_score += comp_play_hand(new_hand, word_list)
                old_hand = new_hand  # Update the old hand with the new one
            elif choice == 'r':
                pc_score += comp_play_hand(old_hand, word_list)
            else:
                print('Your selection was not understood.  Try again... ')
        elif who_plays == 'e':  # exit
            print('Thanks for playing!')
            exit()
        else:
            print('Your selection was not understood.')

    print('Thanks for playing!')
    exit()
#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
