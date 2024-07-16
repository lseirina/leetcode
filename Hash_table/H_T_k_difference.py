"""
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]

 """
from collections import Counter

def find_pairs_with_difference(nums, k):
    my_dict = Counter(nums)
    count = 0

    for num in nums:
        if (num - k) in my_dict:
            count += my_dict[num-k]

    return my_dict



print(find_pairs_with_difference([1,2,2,1,2], 1))




















# from collections import Counter

# def find_pairs(nums, k):
#     dict_nums = Counter(nums)
#     count = 0
#     for num in nums:
#         if num - k in dict_nums:
#             count += dict_nums[num - k]

#     return count

# print(find_pairs([1,2,2,1], 1))