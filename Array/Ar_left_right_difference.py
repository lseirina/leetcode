"""
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
"""

def find_difference(nums):
    n = len(nums)
    left_sum = [0] * n
    right_sum = [0] * n

    for i in range(1, n):
        left_sum[i] = left_sum[i-1] + nums[i-1]
    for i in range(n-2, -1, -1):
        right_sum[i] = right_sum[i+1] + nums[i+1]

    return [abs(left_sum[i] - right_sum[i]) for i in range(n)]

print(find_difference([10,4,8,3]))

































# def find_difference(nums):

#     n = len(nums)
#     left_sum = [0] * n
#     right_sum = [0] * n

#     for i in range(1, n):
#         left_sum[i] = left_sum[i-1] + nums[i-1]

#     for i in range(n-2, -1, -1):
#         right_sum[i] = right_sum[i+1] + nums[i+1]


#     answer = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
#     return answer

# print(find_difference([10,4,8,3]))