"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""
"""
#1 solution
nums = [2,7,11,15]
target = 17
dict_nums = {}
for i, num in enumerate(nums):
    if (target - num) in dict_nums:
        print([dict_nums[target - num], i])
    dict_nums[num] = i

"""
#2 solution
nums = [2,7,11,15]
target = 13

for num in nums:
    if (target - num) in nums:
        print([nums.index(num),nums.index(target - num)])
    