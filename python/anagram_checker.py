import string


def character_occurrences(s):
    occurrences = {}
    for x in string.ascii_uppercase:
        occurrences[x] = 0
    for x in s.upper():
        if x in string.ascii_uppercase:
            occurrences[x] += 1
    return occurrences


def is_anagram(string_1, string_2):
    occurrences_string1 = character_occurrences(string_1)
    occurrences_string2 = character_occurrences(string_2)
    for x in string.ascii_uppercase:
        if occurrences_string1[x] == occurrences_string2[x]:
            return True
        else:
            return False


