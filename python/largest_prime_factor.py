# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(n):
    factors = []
    x = 2
    while x <= n:
        while n % x == 0:
            factors.append(x)
            n = n / x
        x += 1
    largest_factor = max(factors)
    return largest_factor

