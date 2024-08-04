"""
Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

Output: [3,4]

Explanation:

The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.
[2,3,2], nums2 = [1,2]
"""
from collections import Counter


def find_intersaction_value(nums1, nums2):
    s_nums1 = set(nums1)
    s_nums2 = set(nums2)
    answer1 = answer2 = 0

    for num in nums1:
        if num in s_nums2:
            answer1 += 1

    for num in nums2:
        if num in s_nums1:
            answer2 += 1

    return [answer1, answer2]

print(find_intersaction_value([24,28,7,27,7,27,9,24,9,10], [12,29,9,7,5]))
