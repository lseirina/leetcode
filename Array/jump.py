"""
nput: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
def count_jumps(nums):
    jump = 0
    last_position = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if (nums[i] + i) >= last_position:
            jump =





print(count_jumps([2,3,1,1,4]))
