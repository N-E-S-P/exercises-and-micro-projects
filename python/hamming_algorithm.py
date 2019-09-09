def hamming_algorithm(string_1, string_2):

    if len(string_1) == len(string_2):
        substitutions = []
        for pos, letter in enumerate(string_1) and enumerate(string_2):
            if string_1[pos] != string_2[pos]:
                substitutions.append(letter)
        return len(substitutions)

    elif len(string_1) > len(string_2):
        return string_2

    else:
        return string_1