# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome_product():
    palindrome = []
    x = 100
    y = 100
    while x <= 999 and y <= 999:
        n = x * y
        n = str(n)
        if n == n[::-1]:
            palindrome.append(int(n))
        x += 1
        y += 1
    return max(palindrome)


