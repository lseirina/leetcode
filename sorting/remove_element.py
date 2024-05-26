# remove_element([1, 1, 3, 1, 4, 1, 1, 4], 1))
# output: 3 - 3 numbers(3, 4, 4) are not '1'

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return nums

print(remove_element([1, 1, 3, 1, 4, 1, 1], 1))











# def remove_element(nums, val):
#     i = 0
#     while i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#         else:
#             i += 1

#     return len(nums)

# print(remove_element([1, 1, 3, 1, 4, 1, 1, 4], 1))


# def remove_element(nums, val):
#     i = 0
#     while i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#         else:
#             i += 1


#     return len(nums)
# print(remove_element([1,1,1,1], 1))