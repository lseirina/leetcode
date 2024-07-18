"""
return the length of the longest substring between two equal characters, excluding the two characters.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
# """

from collections import Counter


def find_largest_substring(s):
    my_dict = {}
    max_length = -1
    for i, num in enumerate(s):
        if num in my_dict:
            length = i - my_dict[num] - 1
            max_length = max(max_length, length)
        else:
            my_dict[num] = i
    return max_length

print(find_largest_substring("abca"))









# def find_longest_substring(s):
#     first_occurance = {}
#     max_length = -1
#     for i, char in enumerate(s):
#         if char in first_occurance:
#             length = i - first_occurance[char] - 1
#             max_length = max(max_length, length)
#         else:
#             first_occurance[char] = i
#     return max_length
# print(find_longest_substring("abghjca"))



























# def max_length(s):
#     my_dict = {}
#     a = -1
#     for i in range(len(s)):
#         if s[i] in my_dict:
#             a = max(a, (i - my_dict[s[i]] - 1))
#         else:
#             my_dict[s[i]] = i

#     return a


# print(max_length("mgntdygtxrvxjndwksqhxuxtrvm"))