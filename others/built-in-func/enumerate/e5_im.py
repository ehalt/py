#  you want to find the positions of all occurrences of a specific item in a list.

fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']
banana_indices = [index for index, fruit in enumerate(fruits) if fruit == 'banana']
print(banana_indices)