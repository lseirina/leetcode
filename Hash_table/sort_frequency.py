"""
Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
"""
from collections import Counter

def my_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = [num + 1 for num in res]
        return res
    return wrapper

@my_decorator
def sort_frequency(nums):
    cnt = Counter(nums)
    nums.sort(key=lambda x: (cnt[x], -x))

    return nums


print(sort_frequency([2,3,1,3,2]))

def test():
    assert sort_frequency([2,3,1,3,2]) == [2, 4, 4, 3, 3]
    assert sort_frequency([]) == []
    print('Tests passed')

test()
