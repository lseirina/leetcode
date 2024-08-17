"""
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
def find_longest_ones(nums, k):
    max_len = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if right == 0:
            zero_count += 1

        while zero_count > k:
            zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print(find_longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

