"""
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""


def find_increasing_triplets(nums):
    if len(nums) < 3:
        return False

    first = second = float('inf')  # это бесонечноть превращенное в число, т.е. самое большое число

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False


print(find_increasing_triplets([20,100,10,12,5,13]))
