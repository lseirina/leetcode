
# Input: nums = [4, 2, 7, 2, 8, 3, 1, 3]
# Output: [2, 3]


from collections import Counter

def find_duplicate(nums):
    c_nums = Counter(nums)
    res = []
    for num, i in dict(c_nums).items():
        if i != 1:
            res.append(num)

    return res

def test():
    assert find_duplicate([1, 2, 4, 5]) == []
    assert find_duplicate([1, 1, 1, 1, 1]) == [1]
    assert find_duplicate([1, -1]) == []
    assert find_duplicate([2, 3, 2, 4, 5, 5]) == [2, 5]

    print('Tests passed')

test()
print(find_duplicate([4, 3, 2, 7, 8, 3, 2, 1]))












# def find_duplicates(nums):
#     num_counts = {}

#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1

#     duplicates = [num for num, count in num_counts.items() if count > 1]   #list comprehension
#     # duplicates = []
#     # for num, count in num_counts.items():
#     #     if count > 1:
#     #         duplicates.append(num)
#     return duplicates

# print(find_duplicates([1,2,2,1]))

# def test():
#     assert find_duplicates([1,2,2,3]) == [2]
#     assert find_duplicates([1,2,3]) == []
#     assert find_duplicates([]) == []
#     assert find_duplicates([1,1,1,1,1]) == [1]

#     print('Tests passed')

# test()