# Write code that defines the variable number_of_e_in_austen and counts how many times the letter e occurs in text.


def number_of_e_in_austen():
    number_of_e = 0
    text = open("austen-emma-excerpt.txt", "r")
    for letter in text.read():
        if letter == "e" or letter == "E":
            number_of_e += 1
    return number_of_e


