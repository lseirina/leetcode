"""
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
"""





def cc(nums):
    set_nums = set(nums)

    longest_sequence = 0
    for num in nums:
        if num - 1 not in set_nums:
            current_num = num
            current_sequence = 1

            while current_num + 1 in set_nums:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return current_sequence

print(cc([0, 0, -1]))
