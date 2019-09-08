
def multiples_3_or_5(n):
    multiples = []
    if n < 10:
        return 'The number must be equal to 10 or greater.'
    else:
        for x in range(1, n+1):
            if x % 3 == 0 or x % 5 == 0:
                multiples.append(x)
        return multiples


