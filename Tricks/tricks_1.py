"""
        ========= python tricks ============

    wanna check membership ? 
    use -> in <- operator to check if an element is in a list 

    List comprehension for concise and readable list operations 


    enumerate: use enumerate to loop over a list and get both the index and the value 

    // avoid unnecessary loops 

    using any or all : 
    These functions can be used to check if any or all elements in an iterable 
    satisfy a condition 

    using map and filter:
    These functions can help you apply operations to all elements in an iterable 

    // Use list methods 

    append : add an element to the end of the list 
    extend : add multiple elements to the end of the list 
    insert : insert an element at a specific poisition
    remove : Remove the frist occurrence of an element 
    pop : Remove and return an element at a specific position 


    // use dictionary methods


    get : Retrieve a value with a default if the key is not found 
    items : Get a view of dictionary items ( key- value pairs) 
    keys : Get a view of dictionary keys
    values: Get a view of dictionary values 

    // use Ternary operators 

    ans = "Even" if number % 2 == 0 else "Odd" 

    // use zip for parallel Iteration 

    for a, b in zip ( list1, list2):
        print(a, b)


    

"""


# use defaultdict from collections 
from collections import defaultdict

d = defaultdict(int)
d['key'] += 1


# use Counter for requency counting 

from collections import Counter 

c = Counter([1, 1, 2, 3, 4, 5, 2, 1, 3, 4, 5, 6, 6, 8])
print(c)


# use set for uniqueness 

unique_elems = list(set(my_list))


# use lambda functions [ lambda functions can be used for small, anonymous functions ]

sorted_list = sorted(my_list, key = lambda x : x[1])

