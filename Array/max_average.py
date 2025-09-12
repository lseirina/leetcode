"""
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""

def find_max_average(nums, k):
    sum_window = sum(nums[:k])
    max_avg = sum_window/k
    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i-k]
        current_avg = sum_window/k
        max_avg = max(max_avg, current_avg)

    return max_avg




print(find_max_average([1,12,-5,-6,50,3], 4))
