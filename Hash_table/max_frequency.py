"""
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
"""


from collections import Counter


def find_max_frequency(nums):
    count = Counter(nums)
    answer = 0
    for val in count.values():
        if val == max(count.values()):
            answer += val

    return answer


print(find_max_frequency([1,2,2,3,1,4]))
