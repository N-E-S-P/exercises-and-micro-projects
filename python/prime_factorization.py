def prime_factorization(n):
    from collections import Counter
    factors = []
    for x in range(2, n + 1):
        while x <= n:
            if n % x == 0:
                factors.append(x)
                n = n / x
                x = 2
            else:
                x = x + 1
    factors_dict = Counter(factors)
    return factors_dict