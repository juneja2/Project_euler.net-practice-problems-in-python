
#Answer should be like
#(1, 4), (2, 3)

#List shouldn't have any duplicates

def pair_with_sum(list, SUM):

    #First create an empty list that would contain the pair tuple which would hold the pairs
    #Then create an empty complement dictionary which will hold the nums which you would compare with someone else's complement
    #And if they are equal that means we found a pair and we append those as a tuple to pairs list
    pairs = []
    complement_dict = {}
    

    for num in list:
        complement = SUM - num

        if complement in complement_dict.keys():
                pairs.append(tuple((num, complement)))
    
        complement_dict[num] = num

    return pairs

mylist = [1, 3, 2, 5, 46, 6, 7, 4]
sum = 5

print(pair_with_sum(mylist, sum))

mylist = [-2, 5, 9, -1, 10, 22, 21]
print(pair_with_sum(mylist, 20))

#Output 
# [(2, 3), (4, 1)]
# [(22, -2), (21, -1)]
