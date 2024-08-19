"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


def merge_sorted_array(nums1, m, nums2, n):
    # return sorted(nums1[:m] + nums2[:n])
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()
    return nums1


print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))
