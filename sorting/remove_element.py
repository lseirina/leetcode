def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1


    return len(nums)
print(remove_element([1,1,1,1], 1))