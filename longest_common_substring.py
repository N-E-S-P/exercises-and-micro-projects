def longest_common_substring(string_1, string_2):

    same_words = []

    token_string_1 = string_1.split(' ')
    token_string_2 = string_2.split(' ')

    for pos, x in enumerate(token_string_1):
        if x in token_string_2[pos]:
            same_words.append(x)

    if len(same_words) > 0:
        same_words = ' '.join(same_words)
        return same_words
    else:
        return '""'
