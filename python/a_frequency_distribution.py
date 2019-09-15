# write code that counts the number of word tokens in which the letter "a" is present in a small corpus. You need to do
# this on the basis of a frequency distribution of words that is represented by a dictionary. In this dictionary,
# keys are words and values are the frequencies.


def a_frequency_distribution(dictionary):
    number_of_a = 0
    n_a = 0
    for x, y in dictionary.items():
        for z in x:
            if z == "a":
                n_a += 1
        number_of_a += y * n_a
        n_a = 0
    return number_of_a

