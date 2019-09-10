# Create a function that, given a string, returns the percentage of the vowels that are present in the string in
# relation to the total number of the letters in said string.


def vowel_frequency(string):
    vowel_list = []
    for x in string:
        if x in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
            vowel_list.append(x)
    frequency = len(vowel_list) / len(string) * 100
    return frequency
