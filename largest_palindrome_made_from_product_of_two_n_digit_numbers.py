
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


#We don't need this in isPalindrome
def num_digits_in(num):
    num_cpy = num
    num_digits = 0
    while num_cpy != 0:
        num_cpy = int(num_cpy/10)
        num_digits += 1
    return num_digits

def isPalindrome(product):
    #Improvement here: Credits internet
    product_cpy = str(product)
    if str(product) == product_cpy[::-1]:
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

           


