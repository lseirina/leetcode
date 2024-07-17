
"""
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-index.
"""
from collections import Counter

def find_good_pairs(nums):
    my_dict = Counter(nums)
    count = 0

    for num in my_dict.values():
        count += num * (num - 1) // 2

    return count


print(find_good_pairs([1,2,3,1,1,3]))





























# def find_good_pairs(nums):
#     good_pairs = {}
#     count = 0
#     for num in nums:
#         if num in good_pairs:
#             if good_pairs[num] == 1:
#                 count += 1
#             else:
#                 count += good_pairs[num]

#             good_pairs[num] += 1

#         else:
#             good_pairs[num] = 1

#     return count

# print(find_good_pairs([1,1,1,1]))

# def find_good_pairs(nums):
#     freq = collections.Counter(nums)
#     count = 0

#     for num in freq.values():
"""Формула для количества способов выбрать 2 элемента из num элементов (без учёта порядка) — это комбинаторная функция C(num, 2)
, которая определяет сколько существует способов выбрать 2 элемента из этого множества"""
#         count += num * (num - 1) // 2  # the double forward slashes (//) are used for integer division in Python.

#     return count

# print(find_good_pairs([1,1,1,1,3]))
