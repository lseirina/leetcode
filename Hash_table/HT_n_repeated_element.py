
# Input: nums = [1,2,3,1,1,3]
# Output: 2

from collections import Counter

def find_no_repeated_num(nums):
    my_dict = {}
    for num in nums:
        my_dict[num] = my_dict.get(num, 0) + 1
    for num in nums:
        if my_dict[num] == 1:
            return num

print(find_no_repeated_num([1,2,3,1,1,3]))



















def repaeted_n_times(nums):
    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for  num, count in num_counts.items():
        if count > 1:
            return num


print(repaeted_n_times([1,2,3,1,1,3]))