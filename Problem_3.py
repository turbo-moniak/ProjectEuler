# Largest prime factor

# The prime factor of 13195 are 5, 7, 13, 29.
# What is the largest prime factor of the number 600581475143?


def check_if_prime(factor):

    is_prime = True

    for i in range(2, int(factor/2)):
        if factor % i == 0:
            is_prime = False

    return is_prime


def find_largest_prime_factor():

    number = 600851475143
    largest_prime = 0

    for i in range(2, number):
        if number % i == 0:
            factor = i
            is_prime = check_if_prime(factor)
            if is_prime:
                if factor > largest_prime:
                    largest_prime = factor
                    print(largest_prime)


find_largest_prime_factor()