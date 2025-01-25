def find_the_third_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 3:
        return "not enough unique numbers to find the third largest"
    unique_nums.sort()
    return unique_nums[-3]

nums = [3, 3, 2, 1, 5, 7, 9]
result = find_the_third_largest(nums)
print(result)
