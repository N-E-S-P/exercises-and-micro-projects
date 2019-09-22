

def every_term_counter(file):
    counter = {}
    words = open(file, "r").read().split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter
