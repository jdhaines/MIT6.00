# from ps3a import get_word_score

# print(get_word_score('', 5))

# from ps3a import update_hand

# hand = {'j': 2, 'o': 2, 's': 2, 'h': 2, 'y': 2}
# print(update_hand(hand, 'joshy'))

from ps3a import is_valid_word, load_words
word_list = load_words()
# hand = {'j': 2, 'o': 2, 's': 2, 'h': 2, 'y': 2}
hand = {'t': 1, 'r': 2, 'u': 1, 'e': 1, 'p': 2, 'a': 3}
# hand = {'l': 2, 'n': 1, 'v': 2, 'e': 1, 'i': 1}
print(is_valid_word('raaaapture', hand, word_list))
