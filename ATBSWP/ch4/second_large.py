# functional approach 

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers  = [5, 5, 3, 8, 1, 9]
second_largest = find_second_largest(numbers)
print(second_largest)