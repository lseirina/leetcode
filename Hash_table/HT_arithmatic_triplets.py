"""
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.
"""



































# def find_triplet(nums, diff):
#     set_nums = set(nums)
#     count = 0
#     for num in set_nums:
#         if num + diff in set_nums and num + diff * 2 in set_nums:
#             count += 1
#     return count


# print(find_triplet([0,1,4,6,7,10,13, 16], 3))































# def find_arithmatic_triplets(nums: list[int], diff: int | float) -> int:
#     set_nums = set(nums)
#     count = 0
#     for num in set_nums:
#         if (num - diff) in set_nums and num - diff * 2 in set_nums:
#             count += 1

#     return count


# print(find_arithmatic_triplets([0, 1, 4, 6, 7, 10], 3))


# count = 0
# for num in nums:
#     if (num - diff) in nums and (num - diff * 2) in nums:
#         count += 1

# return count
