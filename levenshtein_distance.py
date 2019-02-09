def levenshtein_distance(string_1, string_2):

    operations = 0
    string_1 = list(string_1)
    string_2 = list(string_2)

    if len(string_1) == len(string_2):
        for pos, x in enumerate(string_2):
            if x not in string_1[pos]:
                string_1[pos] = x
                operations = operations + 1
        return operations

    elif len(string_1) > len(string_2):
        for pos, x in enumerate(string_2):
            if x not in string_1:
                string_1[pos] = x
                operations += 1
            elif x not in string_1[pos]:
                if x in string_1[pos+1:]:
                    string_1.pop(pos)
                string_1[pos] = x
                operations += 1
        while len(string_1) > len(string_2):
            string_1.pop()
            operations += 1
        return operations

    elif len(string_1) < len(string_2):
        while len(string_1) < len(string_2):
            for x in string_2[len(string_1):]:
                string_1.append(x)
                operations += 1
        for pos, x in enumerate(string_2):
            if x not in string_1:
                string_1[pos] = x
                operations += 1
            elif x not in string_1[pos]:
                if x in string_1[pos + 1:]:
                    string_1.pop(pos)
                string_1[pos] = x
                operations += 1
        return operations



