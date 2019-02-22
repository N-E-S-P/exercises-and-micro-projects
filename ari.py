# Write an algorithm in Python which takes a string representing a text in input and returns the ARI
# for that text. As a simplification, the input text can be composed only by English characters,
# numbers, commas, semicolons, colons, and full stops, and no abbreviation (such as “e.g.”) can be
# used.


import string
import math
import unidecode


def automated_readability_index(input_string):

    input_string = unidecode.unidecode(input_string)

    split_string = input_string.split('. ')
    sentences = len(split_string)

    split_sent = input_string.split(' ')
    words = len(split_sent)

    chars = 0
    for char in input_string:
        if char in string.ascii_letters or char in string.digits:
            print(char)
            chars += 1

    ari = math.ceil(4.71 * (chars / words) + 0.5 + (words / sentences) - 21.43)
    return ari

