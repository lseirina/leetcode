

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# -  2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

def find_next_greater(nums1, nums2):
    greater_pairs = {}
    stack = []
    res = []
    for num in nums2:
        while stack and stack[-1] < num:
            greater_pairs[stack.pop()] = num
        stack.append(num)

    for element in stack:
        greater_pairs[element] = -1

    for num in nums1:
        if num in greater_pairs:
            res.append(greater_pairs[num])

    return res


print(find_next_greater([2,4], [1,2,3,4]))






























# def find_next_greater(nums1, nums2):
#     greater_pairs = {}
#     stack = []
#     res = []

#     for num in nums2:
#         while stack and stack[-1] < num:
#             greater_pairs[stack[-1]] = num
#             stack.pop()
#         stack.append(num)

#     for element in stack:
#         greater_pairs[element] = -1

#     for num in nums1:
#         res.append(greater_pairs[num])

#     return res


# print(find_next_greater([2,4], [1,2,3,4]))


















# # def next_greater_element(nums1, nums2):
# #     if not nums2:
# #         return None

# #     next_greater = {}
# #     result = []
# #     stack = []

# #     for num in nums2:
# #         while stack and stack[-1] < num:
# #             next_greater[stack[-1]] = num
# #             stack.pop()
# #         stack.append(num)

# #     for element in stack:
# #         next_greater[element] = -1

# #     for num in nums1:
# #         result.append(next_greater[num])

# #     return result

# # print(next_greater_element([2,4,7], [1,7,2,8,5,4,2,3,4,8,5]))

# # def test():
# #     assert next_greater_element([2,4,7], [1,7,2,8,5,4,2,3,4,8,5]) == [3,8,8]
# #     assert next_greater_element([0], [0]) == [-1]
# #     print('Tests passed')

# # test()