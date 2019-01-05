#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#  The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.#

def sum_of_mutiples_of_three_or_5():
    sum = 0
    for i in range(1, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


def sum_of_natural_numbers_upto(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(sum_of_mutiples_of_three_or_5())
print(sum_of_natural_numbers_upto(1000))
#Output
#233168
#499500
