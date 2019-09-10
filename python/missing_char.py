# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n
# will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


def missing_char(s, n):
    if 0 <= n <= len(s) - 1:
        new_string = []
        for pos, x in enumerate(s):
            if pos != n:
                new_string.append(x)
        new_string = ''.join(new_string)
        return new_string
    else:
        return "Out of range!"
