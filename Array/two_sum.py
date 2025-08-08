# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def twoSum(self, nums, target):
    num_map = {}
    n = len(nums)

    for i in range(n):
        num = target - nums[i]
        if num in num_map:
            return [num_map[num], i]
        num_map[nums[i]] = i
