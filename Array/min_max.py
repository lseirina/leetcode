"""
For example, if the input list is [5, 3, 8, 1, 6, 9],
the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value."""
def find_max_min(nums):
    return (min(nums), max(nums))


print(find_max_min([5, 3, 8, 1, 6, 9]))