
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def num_digits_in(num):
    num_cpy = num
    num_digits = 0
    while num_cpy != 0:
        num_cpy = int(num_cpy/10)
        num_digits += 1
    return num_digits

def isPalindrome(product):

    num_digits = num_digits_in(product)
    partition = int(num_digits/2)

    if num_digits % 2 == 0:

        left_half = int(product / (10 ** partition))
        right_half = str(product - left_half * (10 ** partition))[::-1]
        left_half = str(left_half)

        #problem i ran into is when i get something like 9009 the right side after % doesnt't have 09. Instead it had only 9
        #which was a problem which is why I did a little padding myself by adding the right amount of zeros at the end
        #After reversing
        right_half += (len(left_half) - len(right_half)) * '0'
        
        if left_half == right_half:
            return True
    else:
        left_half = str(int(product / (10 ** (partition + 1))))
        right_half = str(product % (10 ** (partition)))
        right_half += (len(left_half) - len(right_half)) * '0'
        if left_half == right_half:
            return True

    return False

def largest_palindrome_made_from_product_of_two_n_digit_numbers(n_digit_number1, n_digit_number2):

    largestProduct = 1
    largest_i = 1
    largest_j = 1
    for i in range (n_digit_number1, 1, -1):
        for j in range (n_digit_number2, 1, -1):
            product = i * j
            if isPalindrome(product) and product > largestProduct:
                largest_i = i
                largest_j = j
                largestProduct = product
            
    return largestProduct, largest_i, largest_j

print(largest_palindrome_made_from_product_of_two_n_digit_numbers(999, 999))

    
#Not very efficient as time complexity is O(n*n)
#O(1) in space

           


