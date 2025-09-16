# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Hello, world')
        return result
    return wrapper
      
@my_decorator  
def twoSum(nums, target):
    num_map = {}
    for i in range(len(nums)):
        if (target - nums[i]) in num_map:
            return [num_map[target-nums[i]], i]
        num_map[nums[i]] = i

    return num_map
    

print(twoSum([2,7,11,15], 9))