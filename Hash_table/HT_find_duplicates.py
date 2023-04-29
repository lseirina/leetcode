
# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]

def find_duplicates(nums):
    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    duplicates = [num for num, count in num_counts.items() if count > 1]   #list comprehension
    # duplicates = []
    # for num, count in num_counts.items():
    #     if count > 1:
    #         duplicates.append(num)



    return duplicates

print(find_duplicates([1,1,1,1]))