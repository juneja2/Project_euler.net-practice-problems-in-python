
def lesser_of_two_evens(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        if n1 < n2:
            return n1
        else:
            return n2
    else:
        if n1 > n2:
            return n1
        else:
            return n2
    
print(lesser_of_two_evens(2, 5))
print(lesser_of_two_evens(2, 4))

def animal_crackers(myanimal):
    words = myanimal.lower().split()

    first_letter_of_first_word = words[0][0]
    i = 1
    discrepancy = False
    while i < len(words):
        if first_letter_of_first_word != words[i][0]:
            discrepancy = True
            break
        i += 1
    return (not discrepancy)

print("Animal Crackers output")
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    return False

print("makes twenty output")
print(makes_twenty(20,10)) # --> True
print(makes_twenty(12,8))  # --> True
print(makes_twenty(2,3))   # --> False

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

print("Old macdonald output\n" + old_macdonald("macdonald"))

def master_yoda(text):

    text_reversed = text[::-1]
    words = text_reversed.split()

    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    
    return ' '.join(reversed_words)

print(master_yoda('I am home'))# --> 'home am I'
print(master_yoda('We are ready'))# --> 'ready are We'

def almost_there(num):
    if (abs(100 - num) <= 10) or (abs(200 - num) <= 10):
        return True
    return False

print(almost_there(90))# --> True
print(almost_there(104))# --> True
print(almost_there(150))# --> False
print(almost_there(209))# --> True


print("\nLevel 2\n")

def has_33(nums):
    my_nums_dict = {}

    for index, num in enumerate(nums):
        if num == 3:
            if (index - 1) in my_nums_dict:
                return True
            else:
                my_nums_dict[index] = 3
    
    return False

print(has_33([1, 3, 3]))# → True
print(has_33([1, 3, 1, 3]))# → False
print(has_33([3, 1, 3]))# → False

##PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    returnText = ''
    for char in text:
        returnText += 3*char
    return returnText

print(paper_doll('Hello'))# --> 'HHHeeellllllooo'
print(paper_doll('Mississippi'))# --> 'MMMiiissssssiiippppppiii'

##BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(n1, n2, n3):
    sum = n1 + n2 + n3

    if n1 == 11 or n2 == 11 or n3 == 11:
        sum -= 10

    if sum <= 21:
        return sum
    else:
        return 'BUST'
    
print(blackjack(5,6,7))# --> 18
print(blackjack(9,9,9))# --> 'BUST'
print(blackjack(9,9,11))# --> 19

#### SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
def summer_69(nums):
    sum = 0
    my_6_dict = {}
    key_array = []
    index = 0

    while index < len(nums):
        if nums[index] == 6 and 9 in nums[index + 1:]:
            
            my_6_dict[index] = 6
            key_array.append(index)

            index += 1

            while 9 in nums[index: ] and len(key_array) != 0:
                if nums[index] == 6:
                    key_array.append(index)
                    my_6_dict[index] = 6

                elif nums[index] == 9:
                    my_6_dict.pop(key_array.pop())

                index += 1
        else:
            sum += nums[index]
            index += 1
    return sum


print(summer_69([1, 3, 5]))# --> 9
print(summer_69([4, 5, 6, 7, 8, 9]))# --> 9
print(summer_69([2, 1, 6, 9, 11]))# --> 14
print(summer_69([6, 6, 9, 6, 9, 9, 9, 6]))

def spy_game(nums):
    sequence = []
    for index, num in enumerate(nums):
        if num == 0 or num == 7:
            sequence.append(num)

    index = 0
    while index < len(sequence):
        if sequence[index] == 0:
            if index + 2 < len(sequence):
                index += 1
                if(sequence[index] == 0):
                    index += 1
                    if(sequence[index] == 7):
                        return True
                    else:
                        index += 1
            else:
                return False
        index += 1

    return False

    
print(spy_game([1,2,4,0,0,7,5]))# --> True
print(spy_game([1,0,2,4,0,5,7]))# --> True
print(spy_game([1,7,2,0,4,5,0]))# --> False
print(spy_game([1, 2, 0, 7, 0, 0, 2, 3, 7])) #True

#COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
def isPrime(num):
    max_divisor = int(num / 2)
    while max_divisor > 1:
        if num % max_divisor == 0:
            return False
        max_divisor -= 1
    return True

def count_primes(num):
    if(num < 2):
        return 0
    
    count = 0
    for i in range(2, num + 1):
        if isPrime(i):
            count += 1
    return count


print(count_primes(100))# --> 25)

def print_big(letter):
    a = "   *\n  * *\n *****\n *   *\n *   *\n"
    b = " *****\n *   *\n *****\n *   *\n *****\n"
    c = " *****\n *\n *\n *\n *****\n"
    d = " *****\n *   *\n *   *\n *   *\n *****\n"
    my_dict = {'A': a, 'B':b, 'C':c, 'D':d}
    print(my_dict[letter.upper()])

print_big('a')
print_big('b')
print_big('c')
print_big('d')