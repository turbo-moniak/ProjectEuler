# Largest palidrome product
# A palindormic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers..


def check_if_palindrome(multiplication):
    is_palindrome = True

    length = int(len(str(multiplication))/2)

    for i in range(length):
        if str(multiplication)[i] != str(multiplication)[len(str(multiplication)) - 1 - i]:
            is_palindrome = False

    return is_palindrome


def find_largest_palindrome():

    largest_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, i + 1):
            multiplication = i * j
            is_palindrome = check_if_palindrome(str(multiplication))
            if is_palindrome and largest_palindrome < multiplication:
                largest_palindrome = multiplication
    print(largest_palindrome)



find_largest_palindrome()

