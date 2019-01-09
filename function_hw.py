import math
import string

def vol(rad):
    return 4 * math.pi * (rad ** 3)/3

print(vol(2))

def ran_check(num, low, high):
    if num in range(low, high + 1):
        print(f'{num} is in the range between {low} and {high}')

def ran_bool(num, low, high):
    return num in range(low, high + 1)

ran_check(5, 2, 7)
print(ran_bool(5, 2, 7))

def up_low(s):
    up = 0
    low = 0
    for char in s:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1

    print("No. of Upper case characters : {}".format(up))
    print("No. of Lower case Characters : {}".format(low))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(len(s))
up_low(s)

def unique_list(sl):
    return list(set(sl))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):  
    mul = 1
    for num in numbers:
        if num != 0 :
            mul *= num
        else:
            return 0
    return mul

print(multiply([1,2,3,-4]))
    
def palindrome(s):
    return s == s[::-1]

print(palindrome('helleh'))

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for char in str1.lower():
        if char in alphabet:
            char_index = alphabet.index(char)
            if char_index + 1 < len(alphabet):
                alphabet = alphabet[:char_index] + alphabet[char_index + 1]
            else:
                return True
    return False

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The quick brown fox "))

