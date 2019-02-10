# The first function is a function that, given a message and an integer as key, cyphers that message by shifting the
# the position of each of its letters by an amount that is equal to the key value.
# The second function is a function that, given a cyphered message and an integer as key, de-cyphers that message by
# shifting the position of each of its letters back into its original amount.

###################################################################
#                                                                 #
# WORKS ONLY FOR UPPERCASE . WILL MAKE IT WORK ON LOWERCASE TOO . #
#                                                                 #
###################################################################


import string


def caesar_cypher_codify(message, key):
    coded = ""
    for x in message:
        if x in string.ascii_uppercase:
            i = ord(x) + key
            if i > ord('Z'):
                i = i - 26
            coded += chr(i)
        else:
            coded += x
    return coded


def caesar_cypher_decodify(coded, key):
    decoded = ""
    for x in coded:
        if x in string.ascii_uppercase:
            i = ord(x) - key
            if i < ord('A'):
                i = i + 26
            decoded += chr(i)
        else:
            decoded += x
    return decoded
