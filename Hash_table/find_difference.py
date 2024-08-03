"""
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
"""
def find_difference(nums1, nums2):
   s_nums1 = set(nums1)
   s_nums2 = set(nums2)

   diff1 = s_nums1 - s_nums2
   diff2 = s_nums2 - s_nums1

   return list(diff1), list(diff2)
print(find_difference([1,2,3, 3], [1, 2, 2]))
