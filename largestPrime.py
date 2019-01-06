#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def largest_prime_factor(num):
    
    if num < 2:
        return Exception("Not a valid num to find the largest prime for")

    divisor = 2
    largest_prime = num
    max_divisor = int(math.sqrt(largest_prime))
    #These are loop control variables

    while divisor <= max_divisor:
        if largest_prime % divisor == 0:
            largest_prime = int(largest_prime/divisor)
            max_divisor = largest_prime/2
            divisor = 2
        else:
            divisor += 1
    
    return largest_prime
    

print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
for i in range(101):
    print(largest_prime_factor(i))
#O(n) solution in time and O(1) in space
#And works. I also wrote a recursive solution but it exceeded recursion depth
