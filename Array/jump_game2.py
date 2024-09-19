"""
nput: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
def count_jumps(nums):
    n = len(nums)
    current_end = 0
    farthest = 0
    jumps = 0

    for i in range(n-1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

        if current_end >= n - 1:
            break

    return jumps


print(count_jumps(([2,3,1,1,4])))
