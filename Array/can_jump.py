"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
[3,2,1,1,0,1]
[2,0,0]
"""
def can_jump(nums):
    last_position = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if (nums[i] + i) >= last_position:
            last_position = i
    return last_position == 0


print(can_jump([3,2,1,0,4]))
