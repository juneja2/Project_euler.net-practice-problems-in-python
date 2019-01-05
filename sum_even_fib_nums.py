def next_fib(fib0, fib1):
    return fib0 + fib1

def sum_even_fib(fib0, fib1, limit):

    sum_fib = 0

    if fib0 % 2 == 0:#If fib0 is even
        if fib0 < limit: #Check if it is less than the limit
            #And if it is add it to the sum
            sum_fib += fib0
        else:   #If it is not less than that means we are either equal to or greater than the limit already
            return sum_fib

    if fib1 % 2 == 0:
        if fib1 < limit: #Check if it is less than the limit
            #And if it is add it to the sum
            sum_fib += fib1
        else:   #If it is not less than that means we are either equal to or greater than the limit already
            return sum_fib

    next_fib_num = next_fib(fib0, fib1)
    even = next_fib_num % 2 == 0

    while next_fib_num < limit:
        #If the next_fib_num is even add it to the sum
        if even:
            sum_fib += next_fib_num

        fib0 = fib1
        fib1 = next_fib_num
        #Change the fib0 and fib1 so that we can get the next fibNum

        next_fib_num = next_fib(fib0, fib1)
        #Get the next_fib_num

        even = next_fib_num % 2 == 0
        #Now check if it is even
    
    return sum_fib
    #return the sum at the end
    
    print(sum_even_fib(1, 2, 4000000))
    //Output = 4613732
