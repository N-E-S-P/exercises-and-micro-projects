

def every_term_counter(file):
    counter = {}
    punctuation = "!""£$%&/()=?^[]*+-@#§.:,;_{}`~''"
    infile = open(file, "r")
    words = infile.read().lower()
    infile.close()
    for marker in punctuation:
        words = words.replace(marker, "")
    for word in words.split():
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    outfile = open("frequency_distribution.txt", "w+")
    for word, frequency in counter.items():
        outfile.write(word + ": " + str(frequency) + "\n")
    outfile.close()
    return outfile
