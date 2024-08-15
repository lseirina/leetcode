"""
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""

def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    # for i in range(k):
    #     window_sum += nums[i]

    max_avg = window_sum / k

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        current_avg = window_sum / k
        max_avg = max(max_avg, current_avg)
        
    return max_avg



print(find_max_average([1,12,-5,-6,50,3], 4))
