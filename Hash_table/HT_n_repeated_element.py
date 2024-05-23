
# Input: nums = [1,2,3,1,1,3]
# Output: 2




















def repaeted_n_times(nums):
    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for  num, count in num_counts.items():
        if count > 1:
            return num


print(repaeted_n_times([1,2,3,1,1,3]))