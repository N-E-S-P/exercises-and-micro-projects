# Write some code that defines the variable counter and counts how often a term (assigned occurs in the the file.


def term_counter(file, term):
    counter = 0
    text = open(file, "r")
    words = text.read().split()
    for word in words:
        if word == term:
            counter += 1
    return counter
