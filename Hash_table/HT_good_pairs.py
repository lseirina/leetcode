import collections
"""
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-index.
"""


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

def find_good_pairs(nums):
    freq = collections.Counter(nums)
    count = 0

    for num in freq.values():
        count += num * (num - 1) // 2  # the double forward slashes (//) are used for integer division in Python.

    return count

print(find_good_pairs([1,1,1,1,3]))
