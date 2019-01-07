def first_recurring_character(myStr):
    # myStr = A B C B A
    #         ^       ^
    #Start with a pointers like this and bring the right pointer close to left pointer
    #And if they cross this means we haven't found any recurring element
    #So we update them again increasing l by 1 and setting r to the last char
    #We continually do this until we find the char and if we don't then 
    #We return None
    l = 0
    r = len(myStr) - 1
    while l < r:
        while l < r:
            if myStr[l] == myStr[r]:
                return myStr[l]
            r = r - 1
        l = l + 1
        r = len(myStr) - 1
    return None
print(first_recurring_character("ABCBA"))
print(first_recurring_character("BCABA"))
print(first_recurring_character("ABC"))
