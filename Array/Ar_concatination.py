"""
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""
def concatinate_array(nums):
    nums.extend(nums)
    return nums

print(concatinate_array([1,2,1]))













# def find_concatination(nums):
#     return nums + nums

# print(find_concatination([1,2,1]))
