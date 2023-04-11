"""
    nums = [1, 2, 3, 4, 5]
target = 9
 should print [1, 3], 1 + 3 + 5 = 9, so 2 and 4 we put away
"""
def subarray_sum(nums, target):
    dic_nums = {}
    
    for i, num in enumerate(nums):
        dic_nums[num] = i
        
    return dic_nums


print(subarray_sum([1, 2, 3, 4, 5], 9))