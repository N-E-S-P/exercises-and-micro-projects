

def file_reader(file):
    infile = open(file, "r")
    text = infile.read()
    infile.close()
    return text
