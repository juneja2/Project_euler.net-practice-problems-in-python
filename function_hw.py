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

    # Convert all the character into lower case
    # Then create a set of those character so that we don't check for the same element repeatedly
    # Then check if char is in alphabet which implies that the character we are looking at is an alphabet
    # Then get the index of the alphabet in alphabet string
    # Now we need to remove this char from alphabet
    # In order to do that we have to check if the char is at the end of the string
    # If it is then we just go to the else clause
    # If it isn't then we check if the length of alphabet is 1. This would mean we have 
    # all the characters from A - Z and we return True
    # Lastly if none of the above
    # We change the remove that char from the alphabet as we did in if clause
    # If we go through the entire for loop that means that len(alphabet) > 1 after removing the char
    # which implies that some alphabets are missing from str1 which implies that it isn't a pangram
    # which is why we return False at the end)
    for char in set(str1.lower()):

        if char in alphabet:
            char_index = alphabet.index(char)

            if char_index + 1 < len(alphabet):
                alphabet = alphabet[:char_index] + alphabet[char_index + 1]
            elif len(alphabet) == 1:
                return True
            else:
                alphabet = alphabet[:char_index]

    return False

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The quick brown fox "))
print(ispangram(string.ascii_lowercase))
print(ispangram(string.ascii_uppercase))

