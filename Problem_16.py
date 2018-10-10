# Power digit sum
# 2^15 = 32768 and the sum of its digis is 3 + 2 + 7 + 8 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

from math import pow


def power_digit_sum():

    power = 1000
    base = 2

    power_result = int(pow(base, power))
    sum_of_digits = 0
    for i in range(len(str(power_result))):
        sum_of_digits = sum_of_digits + int(str(power_result)[i])
    print(sum_of_digits)


power_digit_sum()
