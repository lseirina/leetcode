"""
Input: nums = [1,0,1,1], k = 1
Output: true
 nums[i] == nums[j] and abs(i - j) <= k.
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def check_nearby_duplicates(nums, k):
    count_duplicates = {}
    for i in range(len(nums)):
        if nums[i] in count_duplicates:
            count_duplicates[nums[i]].append(i)
        else:
            count_duplicates[nums[i]] = [i]

    for val in count_duplicates.values():
        if len(val) > 1:
            for i in range(len(val)-1):
                if abs(val[i] - val[i+1]) <= k:
                    return True
    return False


print(check_nearby_duplicates([1,2,3,1,2,3], 2))