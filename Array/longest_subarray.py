
"""
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
"""

def find_longest_subarray(nums):
    max_len = 0
    left = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left)

    return max_len


print(find_longest_subarray([0,1,1,1,0,1,1,0,1]))
