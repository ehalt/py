# find common elements in two lists 
'''
    Write a Python function that takes two lists as input and returns 
    a new list containing the common elements between them.
    The order of the elements in the output list should match their order in the first list.
'''


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = []
for i in range(len(list1)): 
    for j in range(len(list2)):
        if (list1[i] == list2[j]) : # compare elements directly
            result.append(list1[i]) # append matching element


print(result)



# another approach  ( functional )


def find_common_elem(list1, list2) :
    return [item for item in list1 if item in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elem = find_common_elem(list1, list2)
print(common_elem)








