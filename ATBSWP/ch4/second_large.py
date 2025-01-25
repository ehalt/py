# functional approach 

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers = [10, 20, 4, 45, 99, 99]
second_largest = find_second_largest(numbers)
print(second_largest)