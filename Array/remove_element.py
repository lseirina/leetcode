"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def remove_element(nums, val):

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)

    return len(nums)

    # i = 0 тоже верно
    # for j  in range(len(nums)):
    #     if nums[j] != val:
    #         nums[i] = nums[j]
    #         i += 1
    # return i
        

print(remove_element([0,1,2,2,3,0,4,2], 2))
