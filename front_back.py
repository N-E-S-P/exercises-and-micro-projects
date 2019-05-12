# Given a string, return a new string where the first and last chars have been exchanged.


def front_back(s):
    if len(s) > 1:
        s = ''.join([s[-1], s[1:-1], s[0]])
        return s
    else:
        return s
