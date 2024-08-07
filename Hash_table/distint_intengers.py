"""
Input: nums = [1,13,10,12,31]
Output: 6
Explanation: After including the reverse of each number, the resulting array is [1,13,10,12,31,1,31,1,21,13].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).
"""
def count_distinct_integers(nums):
    res = []
    for num in nums:
        res.append(str(num)[::-1])
    for num in res:
        nums.append(int(num))

    return len(set(nums))


print(count_distinct_integers([1,13,10,12,31]))