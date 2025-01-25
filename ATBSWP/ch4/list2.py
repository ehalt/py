list = [1, 2, 3, 4, 5]
print(list)


mixed_list = [1, "hello", 3.14, True]
print(mixed_list)





# accessing list elements 

my_list = [10, 20, 30, 40, 50]
print(my_list)
#access first element
print(my_list[0])
#acess the third element
print(my_list[2])

#negative indexing 
print(my_list[-1])
print(my_list[-2])








'''
    slicing a list 

    list[start:stop:step]

    start : from the index to start slicing ( inclusive )
    stop : from the index to stop slicing (exclusive )
    step : interval between elements ( optional )
'''

list = [10, 20, 30, 40, 50]

#slice from index 1 to 3 [exclusive]
print(list[1:3])

# slice from the beginning to index 3 [exclusive]
print(list[:3])

# slice from index 2 to end 
print(list[2:])

# slice with a step of 2 
print(list[::2])

# reverse the list 
print(list[::-1])

















'''
    modifying a list 

    list are mutable, ( liable to change. ) 
    so i can change their elements 
'''

list = [10, 20, 30, 40, 50]

# chnage the second element 
list[1] = 300
print(list)

# modify multiple elements using slicing 
list[1:3] = [200, 400]
print(list)











'''
    adding elements to a list 

    append() : adds an element to the end of the list 
    insert() : insert an element at a specific index
    extend() : adds multiple elements ( from another list ) to the end
'''

list = [1, 2, 3]
# append an element
list.append(4)
print(list)

# insert an element at index 1
list.insert(1, 10)
print(list)

# extend the list with another list
list.extend([5, 6, 7])
print(list)











'''
        removing elements from a list 

        remove() : removes the first occurrence of a value 
        pop() : removes and returns the elements at a specific index ( default is the last element )
        del : delets an elemnets or a slice of elements 

'''

list = [10, 20, 30, 40, 50]

# remove the first occurrence of 20
list.remove(20)
print(list)

# remove and return the last element 
popped_elem = list.pop()
print(popped_elem)
print(list)

# remove the element at index 1 
del list[1]
print(list)











'''
        list operations 

'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

#concatenation
combined_list = list1 + list2
print(combined_list)

# repetition
repeated_list = list1 * 2
print(repeated_list)

# membership check 
print(3 in list1)
print(10 in list1)








'''
    list methods 



    append() : adds an element to the end of the list 
    insert() : inserts an element at a specific index
    extend() : adds multiple elements to the end of the list 
    remove() : removes the first occurrence of a value 
    pop()    : removes and returns an element at a given index
    clear()  : removes all elements from the list 
    index()  : returns the index of the first occurrence of a value 
    count()  : returns the number of occurrences of a value 
    sort()   : sorts the list in ascending order
    reverse(): reverses the order of the list 
    copy()   : returns a shallow copy of the list 

    
'''







# create a list of squares 
squares = [x ** 2 for x in range(10)]
print(squares)

# create a list of even numbers 
evens = [x for x in range(20) if x % 2 == 0]
print(evens)











'''
    nested lists

    lists can contain other lists, creating nested ( multi-dimensional ) lists


'''

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list[0][1])











'''
        common list functions 

        len() : returns the number of elements in the list 
        min() : returns the smallest element in the list 
        max() : returns the largest element in the list 
        sum() : returns the sum of all elements in the list

'''



my_list = [10, 20, 30, 40, 50]

print(len(my_list))  # Output: 5
print(min(my_list))  # Output: 10
print(max(my_list))  # Output: 50
print(sum(my_list))  # Output: 150









'''
    copying a list 
    Be careful when copying lists, as assigning a list to a new variable creates a 
    reference, not a copy. Use the copy() method or slicing to create a new list.

'''

#shallow copy using copy()

original = [1, 2, 3]
new = original.copy()
new[0] = 100
print(original)
print(new)









'''

    iterating over a list 

'''

list = [10, 20, 30, 40, 50]

for item in list : 
    print(item)



'''
        list vs other DS 

        lists
        tuples
        sets
        dictionaries
'''
