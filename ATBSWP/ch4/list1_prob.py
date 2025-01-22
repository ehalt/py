'''
        --- problem ---

# Example 1
lst = [1, 2, 3, 4, 5, 6, 7]
start = 2
end = 5
print(slice_and_reverse(lst, start, end))
# Output: [6, 5, 4]

# Example 2
lst = ['a', 'b', 'c', 'd', 'e']
start = 1
end = 3
print(slice_and_reverse(lst, start, end))
# Output: ['d', 'c', 'b']

'''


# def solve(lst, start, end):
#     print(lst[start:end])
#     for i in range(len(lst), -1, -1):
#         print(lst[i])

# lst = ['a', 'b', 'c', 'd', 'e']
# solve(lst, 1, 3)


def sliceandreverse(lst: list, start : int, end : int) -> list: 
    return lst[start:end + 1][::-1]


lst = [1, 2, 3, 4, 5, 6, 7]
start = 2
end = 5
print(sliceandreverse(lst, start, end))



