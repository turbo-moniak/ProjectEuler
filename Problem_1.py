# Multiples of 3 and 5
# If we list all natural numbers belowe 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


def find_sum_of_multiples():
    sum_of_multiples = 0
    stop = 1000

    for i in range(stop):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples = sum_of_multiples + i
    print("The sum of multiples is: " + str(sum_of_multiples))


find_sum_of_multiples()