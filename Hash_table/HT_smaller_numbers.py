
"""
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""


def sort_from_biggest_to_smallest(nums: list) -> list:
    my_dict: dict = {}
    res: list = []
    s_nums = sorted(nums)
    for i in range(len(s_nums)):
        if s_nums[i] not in my_dict:  # при формировании словаря, если число уже встречалось, оно не будет перезаписано и 2:1 останется, а не перезапишется на 2:2
            my_dict[s_nums[i]] = i
    for num in nums:
        res.append(my_dict[num])

    return res


print(sort_from_biggest_to_smallest([8,1,2,2,3]))



# #     temp = sorted(nums)
# #     mapping = {}
# #     result = []


# #     for i in range(len(temp)):
# #         if temp[i] not in mapping:
# #             mapping[temp[i]] = i
# #     for num in nums:
# #         result.append(mapping[num])

# #     return result



# print(smaller_numbers_then_current([8,1,2,2,3]))
