"""
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1.
No two values have the same number of occurrences.
"""

from collections import Counter

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is True:
            print("Hello")
        return result
    return wrapper

@decorator
def check_unique_occurences(nums):
    count_nums = Counter(nums)
    if len(set(count_nums.values())) == len(set(nums)):
        return True
    return False




print(check_unique_occurences([1,2,2,1,3,2]))
