import random
n_to_guess = random.randint(0, 10)


def guess_the_number(n):
    if n < n_to_guess:
        print("The number is higher!")
        n = int(input("Try again: "))
        return guess_the_number(n)
    elif n > n_to_guess:
        print("The number is lower!")
        n = int(input("Try again: "))
        return guess_the_number(n)
    elif n == n_to_guess:
        return "Yay! You did it!"
