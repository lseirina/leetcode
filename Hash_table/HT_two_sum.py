"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""


nums = [1, 2, 3, 4, 5]
target = 10
dict_nums = {}
for i, num in enumerate(nums):
    if (target - num) in dict_nums:
        print([dict_nums[target - num], i])
    dict_nums[num] = i



    