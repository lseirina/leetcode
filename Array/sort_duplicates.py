"""Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Function call: new_length = remove_duplicates(nums)
Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3,"""


def sort_duplicates(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1

    return i


test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(sort_duplicates(test4))


# def sort_duplicates(nums): not right
#     count = []
#     for num in nums:
#         if num not in count:
#             count.append(num)

#     return len(count)


# print(sort_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
