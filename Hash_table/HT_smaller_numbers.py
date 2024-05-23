
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
import copy
def count_smaller_numbers(nums):
    my_dict: dict[int] = {}
    res = []
    nums1 = copy.deepcopy(nums)
    for num in sorted(nums1, reverse=True):
        my_dict[num] = len(nums1)-1
        nums1.pop()

    for num in nums:
        res.append(my_dict[num])

    return res



print(count_smaller_numbers([8,1,2,2,3]))






























def smaller_numbers_then_current(nums):
#def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_dict = {}
        result = []
        new_nums = sorted(nums)
        for i, num in enumerate(new_nums):
            if num not in my_dict:
                my_dict[num] = i

        for num in nums:
            result.append(my_dict[num])

        return result













#     temp = sorted(nums)
#     mapping = {}
#     result = []


#     for i in range(len(temp)):
#         if temp[i] not in mapping:
#             mapping[temp[i]] = i
#     for num in nums:
#         result.append(mapping[num])

#     return result



print(smaller_numbers_then_current([8,1,2,2,3]))
