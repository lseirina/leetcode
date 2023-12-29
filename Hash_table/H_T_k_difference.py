"""
Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]

"""


from collections import Counter


from collections import defaultdict, Counter


def count_pairs(nums, k):
    dict_nums = Counter(nums)
    count = 0

    for num in nums:
        if num - k in dict_nums:
            count += dict_nums[num - k]

    return dict_nums


print(count_pairs([1,2,2,1], 1))