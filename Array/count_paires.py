"""
Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
"""


def count_pairs(nums, target):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] < target:
                count += 1

    return count


print(count_pairs([-1,1,2,3,1], 2))
