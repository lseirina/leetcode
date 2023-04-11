"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

def two_sum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        if (target - num) in num_map:
            return [i, num_map[(target - num)]]
        else:
            num_map[num] = i
            
print(two_sum([2,7,11,15], 9))




























#

    