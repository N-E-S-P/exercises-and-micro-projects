# VERBOSE VERSION

def is_palindromic(word):

    word_half = len(word) // 2
    first_half = list(word[0:word_half])
    second_half = list(word[word_half:])
    if len(second_half) != len(first_half):
        second_half.pop(0)
    second_half.reverse()
    if first_half == second_half:
        return True
    else:
        return False


# SMARTER VERSION

def is_palindromic(word):
    
    if word == word[::-1]:
        return True
    else:
        return False
