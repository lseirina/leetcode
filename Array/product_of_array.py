"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


def product_of_array(nums):
    n = len(nums)
    answer = [1] * n

    # Left pass
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Right pass
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

print(product_of_array([1,2,3,4]))





# import math

# def product_of_array(nums):
#     res = [0] * len(nums)
#     for i in range(len(nums)):
#         if i == 0:
#             res[i] = math.prod(nums[i+1:])
#         elif i == len(nums) - 1:
#             res[i] = math.prod(nums[:i])
#         else:
#             res[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])

#     return res

# print(product_of_array([1,2,3,4]))