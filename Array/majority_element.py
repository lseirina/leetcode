"""
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter

def find_majority_element(nums):
    count = Counter(nums)
    for k, v in count.items():
        if v == max(count.values()):
            return k


print(find_majority_element([2,2,1,1,1,2,2]))
