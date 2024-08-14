"""
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
[2,2,2,3,1,1,4,1]
"""
from collections import Counter


def find_max_operation(nums, k):
    freq = Counter(nums)
    count = 0
    for num in nums:
        complement = k - num
        if freq[num] > 0 and freq[complement] > 0:
            if num == complement:
                if freq[num] >= 2:
                    count += 1
                    freq[num] -= 2

            else:
                count += 1
                freq[num] -= 1
                freq[complement] -= 1

    return count


print(find_max_operation([2,2,2,3,1,1,4,1], 4))
