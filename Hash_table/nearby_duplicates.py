"""
Input: nums = [1,0,1,1], k = 1
Output: true
 nums[i] == nums[j] and abs(i - j) <= k.
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def check_nearby_duplicates(nums, k):
    count_duplicates = {}
    for i, num in enumerate(nums):
        if num in count_duplicates and abs(count_duplicates[num] - i) <= k:
            return True
        else:
            count_duplicates[num] = i
    return False


print(check_nearby_duplicates([1,2,3,1,2,3], 2))