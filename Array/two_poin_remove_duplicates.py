"""
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def remove_duplicates(nums):
    j = 1
    for i in range(len(nums)):
        if j == 1 or nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1

    return j


print(remove_duplicates([1,1,1]))
