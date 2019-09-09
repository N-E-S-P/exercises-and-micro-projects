# Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


def collatz_conj(n):
    steps = 0
    if n <= 1:
        return None
    else:
        while n > 1:
            if n % 2 == 0:
                n = n / 2
                steps += 1
            else:
                n = (n * 3) + 1
                steps += 1
        return steps


