"""
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""

def find_pivote_index(nums):
    left_sum = 0
    total_sum = sum(nums)
    for i in range(len(nums)):
        if left_sum == total_sum - left_sum - nums[i]:
            return i
        else:
            left_sum += nums[i]
    return -1


print(find_pivote_index([1,7,3,6,5,6]))