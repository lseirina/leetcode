"""
Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).
"""

def count_good_pairs(nums1, nums2, k):
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            if num1 % (num2 * k) == 0:
                count += 1

    return count


print(count_good_pairs([1, 2, 4, 12], [2, 4], 3))